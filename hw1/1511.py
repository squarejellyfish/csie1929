fuck = [int(x) for x in input().split()]
n, x, y = fuck[0], fuck[1], fuck[2]

if (n % 2 == 1):
    print(20 + (n // 2 + 1)*x - (n // 2)*y)
else:
    print(20 + (n // 2)*x - (n // 2 - 1)*y)

