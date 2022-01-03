import csv

input_filename_1 = "./data/news_articles_small_alphanumerical_jaccard.csv"
input_filename_2 = "./data/news_articles_small_alphanumerical_estimated_jaccard.csv"
input_data1 = set()
data1_dict = {}
similarity1 = 0.8
input_data2 = set()
data2_dict = {}



# Read input
with open(input_filename_1, 'r') as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        # Skip header
        if row[0] != "ID1":
            data1_dict[(row[0], row[1])] = float(row[4])
            data1_dict[(row[1], row[0])] = float(row[4])
            if float(row[4]) > similarity1:
                input_data1.add((row[0], row[1]))
                input_data1.add((row[1], row[0]))


# Read input
with open(input_filename_2, 'r') as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        # Skip header
        if row[0] != "ID1":
            data2_dict[(row[0], row[1])] = float(row[2])
            data2_dict[(row[1], row[0])] = float(row[2])
            input_data2.add((row[0], row[1]))
            input_data2.add((row[1], row[0]))

print("Missing data:", input_data1.difference(input_data2))
print("Excess data:", input_data2.difference(input_data1))

for data in input_data1.difference(input_data2):
    print(data, data1_dict[data])