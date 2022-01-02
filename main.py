import csv

import minhash
import shingling
import candidate_pairs

input_filename = "./data/news_articles_small_alphanumerical.csv"
shingle_size = 2  # Amount of words in each shingle
amount_of_hashes = 100  # Signature length M
rows_per_band = 2  # r
amount_of_bands = int(
    amount_of_hashes / rows_per_band)  # It is assumed that the user ensures that this division results in an integer.

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

# Create shingles
for row in input_data:
    id_shingles.append([row[0], shingling.shingle(row[1], shingle_size)])

# List of lists. Each sublist has article id as first element and list of minhashes as second element.
# The hash functions used to generate the hashes do not change between calls to minhash if amount_of_hashes is
# not changed. If you take element i of the minhashes of two articles, those were generated with the same hashfunction.
minhashes = {}

# Calculate minhashes
for row in id_shingles:
    minhashes[row[0]] = minhash.minhash(row[1], amount_of_hashes)

# TODO: Actually get the data we need from this.
# Examples of checking if articles are candidate pairs/likely plagiarism.
print(candidate_pairs.is_candidate_pair(amount_of_hashes,rows_per_band,minhashes,"84","458"))  # Jaccard > 0.93
print(candidate_pairs.is_candidate_pair(amount_of_hashes,rows_per_band,minhashes,"84","459"))  # Jaccard == 0.1

# TODO: test more parameters (see top of file)
# TODO: compare to Jaccard ('...  here will be used as ground-truth data to evaluate the LSH system...')
# TODO: make function to print result.csv