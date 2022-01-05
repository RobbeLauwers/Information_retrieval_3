import csv

# Copies first two columns from first file to second file, removing duplicates. Adds headers expected in result.csv
filename = ["./data/news_articles_large_alphanumerical_plagiarism.csv", "./result.csv"]

# https://www.programiz.com/python-programming/csv
with open(filename[0], 'r') as input_file:
    with open(filename[1], "w+", newline="\n") as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        written_pairs = set()
        writer.writerow(["doc_id1","doc_id2"])
        header_done = False
        for row in reader:
            if not header_done:
                header_done = True
                continue
            smallest = min(int(row[0]),int(row[1]))
            largest = max(int(row[0]),int(row[1]))
            if (largest,smallest) not in written_pairs:
                written_pairs.add((largest,smallest))
                writer.writerow([str(largest),str(smallest)])

