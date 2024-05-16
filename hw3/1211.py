def swap(l):
    l[0], l[1] = l[1], l[0]

lst = [int(input()), int(input())]
swap(lst)

print(lst[0])
print(lst[1])
