import csv

file = open("fuck.csv", "r")
content = csv.reader(file)
content_row = []
for row in content:
    content_row.append(row)

file = open("dick.csv", "w+")
writer = csv.writer(file)
for row in content_row:
    writer.writerow(row)
file.close()

file = open("dick.csv", "r")
for row in file.readlines():
    print(row)


