import csv
from math import sqrt

name = input()

fail = []
with open(name, "r") as file:
    next(file)
    rows = csv.reader(file)

    for row in rows:
        uid, score = int(row[0]), int(row[1])
        if (sqrt(score) * 11 < 60):
            fail.append(uid)

fail.sort()
print(*fail, sep=" ")
