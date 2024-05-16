import csv

file1 = open("../app/math_list.csv", "r", encoding="big5")
file2 = open("../app/english_list.csv", "r", encoding="big5")
next(file1)
next(file2)

file1 = csv.reader(file1)
file2 = csv.reader(file2)

stds1, stds2 = set([data[0] for data in file1]), set([data[0] for data in file2])

alll = stds1.union(stds2)
both = stds1.intersection(stds2)
one = alll.difference(both)
a = alll.difference(stds2)
b = alll.difference(stds1)

print(sorted(list(both)))
print(sorted(list(one)))
print(sorted(list(a)))
print(sorted(list(b)))
print(sorted(list(alll)))
