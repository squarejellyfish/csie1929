def return2num(n=0)->tuple:
    ret1, ret2 = 1, 0
    for i in range(1, n + 1):
        ret1 *= i
        ret2 += i
    return (ret1, ret2)

n = int(input())
p1, p2 = return2num(n)
print(p1)
print(p2)
