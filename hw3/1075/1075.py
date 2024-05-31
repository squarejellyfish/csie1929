f1, f2 = "../app/{}".format(input()), "../app/{}".format(input())

f1, f2 = open(f1, "r"), open(f2, "r")
content1, content2 = [int(x) for x in f1.read().split()], [int(x) for x in f2.read().split()]
content1.extend(content2)
content1.sort()

for num in content1:
    print("{} ".format(num), end="")
print()
