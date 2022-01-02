import csv

filenames = ["./data/news_articles_small_alphanumerical.csv","./data/news_articles_small_alphanumerical_jaccard.csv"]

csv_list = []



with open(filenames[0], 'r') as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        csv_list.append(row)

with open(filenames[1],'w+',newline="\n") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["ID1","ID2","union","intersect","jaccard"])
    for row1_index in range(len(csv_list)):
        row1 = csv_list[row1_index]
        if row1[0] == "News_ID":
            continue
        for row2_index in range(row1_index+1,len(csv_list)):
            row2 = csv_list[row2_index]
            if row2[0] == "News_ID":
                continue
            if row1[0] != row2[0]:
                article_1 = row1[1].lower()
                article_2 = row2[1].lower()
                set_1 = set(article_1.split(' '))
                set_2 = set(article_2.split(' '))
                union_size = len(set_1.union(set_2))
                intersection_size = len(set_1.intersection(set_2))
                jaccard_index = intersection_size/union_size
                writer.writerow([row1[0],row2[0],union_size,intersection_size,jaccard_index])
