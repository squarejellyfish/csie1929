from cls import cls

foo = input().split(", ")
students = [f.replace("'", "") for f in foo]
c = cls(students)
c.show()

op = input()
if (op == "A"):
    c.groupA()
elif (op == "B"):
    idx = int(input())
    c.groupB(idx)
elif (op == "C"):
    idx = [int(x) for x in input().split()]
    c.groupC(*idx)

c.show()
