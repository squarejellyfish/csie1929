_ = [int(x) for x in input().split()]
l, s = _[0], _[1]
step = 0

while (s != l):
    if (s < l):
        s = s + 5
        step = step + 1
    elif (s > l and s - 2 > 0):
        s = s - 2
        step = step + 1

print(step)
