import csv

import minhash
import shingling
import candidate_pairs
import signature_to_bucket
import time

use_actual_buckets = True
input_filename = "./data/news_articles_small_alphanumerical.csv"
output_filename = "./data/news_articles_small_alphanumerical_estimated_jaccard.csv"
shingle_size = 3  # Amount of words in each shingle
rows_per_band = 6  # r
amount_of_bands = 50 # b
amount_of_hashes = amount_of_bands * rows_per_band  # Signature length M

estimated_s = (1/amount_of_bands)**(1/rows_per_band) # Formula source
print(estimated_s)
# https://towardsdatascience.com/locality-sensitive-hashing-how-to-find-similar-items-in-a-large-set-with-precision-d907c52b05fc

# TODO: calculate s
# TODO: plot Jaccard

# List of lists. Each sublist has article id as first element and article contents as second element.
input_data = []

# Read input
with open(input_filename, 'r') as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        # Skip header
        if row[0] != "News_ID":
            input_data.append(row)

# List of lists. Each sublist has article id as first element and list of article shingles as second element.
id_shingles = []

start_shingling_time = time.time()

# Create shingles
for row in input_data:
    id_shingles.append([row[0], shingling.shingle(row[1], shingle_size)])

# List of lists. Each sublist has article id as first element and list of minhashes as second element.
# The hash functions used to generate the hashes do not change between calls to minhash if amount_of_hashes is
# not changed. If you take element i of the minhashes of two articles, those were generated with the same hashfunction.
minhashes = {}

start_minhash_time = time.time()

# Calculate minhashes
for row in id_shingles:
    minhashes[row[0]] = minhash.minhash(row[1], amount_of_hashes)

start_candidate_pair_time = time.time()


# Iterate over every pair in the dataset and perform LSH check
# TODO: Would this be faster if iterating over everything once and using actual buckets
potential_plagiarism = []
if not use_actual_buckets:
    for i in range(len(input_data)):
        for j in range(i):
            if candidate_pairs.is_candidate_pair(amount_of_hashes, rows_per_band, minhashes, input_data[i][0], input_data[j][0]):
                potential_plagiarism.append((input_data[i][0], input_data[j][0]))
else:
    bucket_data = signature_to_bucket.to_bucket(amount_of_hashes,rows_per_band,minhashes)
    for band_nr, band in bucket_data.items():
        for hash, IDs in band.items():
            for i in range(len(IDs)):
                for j in range(i):
                    potential_plagiarism.append((input_data[int(IDs[i])][0], input_data[int(IDs[j])][0]))


start_refine_time = time.time()

# Refine plagiarism list by using
# Calculate jaccard distance estimate from minhash using J = |A V B| / |A U B|-
plagiarism = []
for plagiarism_couple in potential_plagiarism:
    intersect = set(minhashes[plagiarism_couple[0]]).intersection(set(minhashes[plagiarism_couple[1]]))
    union = set(minhashes[plagiarism_couple[0]]).union(set(minhashes[plagiarism_couple[1]]))
    jaccard_distance = len(intersect)/len(union)
    plagiarism.append((plagiarism_couple, jaccard_distance))

end_time = time.time()
print("Runtime from shingling to finding candidate pairs: " + str(end_time - start_shingling_time))

with open(output_filename,'w+',newline="\n") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["ID1","ID2","jaccard estimate"])
    for index in range(len(plagiarism)):
        id1 = plagiarism[index][0][0]
        id2 = plagiarism[index][0][1]
        jaccard_estimate = plagiarism[index][1]
        writer.writerow([id1,id2,jaccard_estimate])



# TODO: Actually get the data we need from this.
# Examples of checking if articles are candidate pairs/likely plagiarism.
print(candidate_pairs.is_candidate_pair(amount_of_hashes,rows_per_band,minhashes,"84","458"))  # Jaccard > 0.93
print(candidate_pairs.is_candidate_pair(amount_of_hashes,rows_per_band,minhashes,"84","459"))  # Jaccard == 0.1

# TODO: test more parameters (see top of file)
# TODO: compare to Jaccard ('...  here will be used as ground-truth data to evaluate the LSH system...')
# TODO: make function to print result.csv