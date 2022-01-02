import csv
import re

filenames = [["./data/news_articles_large.csv", "./data/news_articles_large_alphanumerical.csv"],
             ["./data/news_articles_small.csv", "./data/news_articles_small_alphanumerical.csv"]]

for filename in filenames:
    # https://www.programiz.com/python-programming/csv
    with open(filename[0], 'r') as input_file:
        with open(filename[1], "w+", newline="\n") as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            for row in reader:
                # https://stackoverflow.com/a/1276774
                # https://stackoverflow.com/a/1546244
                writer.writerow([row[0], re.sub(' +', ' ', re.sub(r'[^a-zA-Z0-9 ]', '', row[1])).lower()])
