foo = [int(x) for x in input().split()]
a, b = foo[0], foo[1]

p = 0
for num in range(a, b + 1):
    if (num % 7 == 0):
        if (p == 0):
            print(num, end='')
            p = 1
        else:
            print(" & {}".format(num), end='')

print()

p = 0
for num in range(a, b + 1):
    if ('7' in str(num)):
        if (p == 0):
            print(num, end='')
            p = 1
        else:
            print(" & {}".format(num), end='')

print()
