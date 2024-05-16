import csv

name = int(input())
name = "./stores_old{}.csv".format(name)

with open(name, newline="", encoding="big5") as file:
    rows = csv.reader(file)
    file_new = open(name.replace("old", "new"), "w", encoding="utf-8")
    writer = csv.writer(file_new, lineterminator=",\n")

    content = [[row[0], row[3], row[5], row[6]] for row in rows]
    writer.writerows(content)
    file_new.close()

with open(name.replace("old", "new"), "r") as file:
    for row in file.readlines():
        print(row, end="")
