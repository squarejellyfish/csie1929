m = int(input())
s1, s2 = map(int, input().split())

car = [0 for _ in range(m)]
car[s1 - 1], car[s2 - 1] = 1, 2

while True:
    print(car)
    g = int(input())
    if (g == -1): break

    d1, d2 = abs(s1 - g), abs(s2 - g)
    if (d1 < d2):
        car[s1 - 1] = 0
        car[g - 1] = 1
        s1 = g
    elif (d2 < d1):
        car[s2 - 1] = 0
        car[g - 1] = 2
        s2 = g
    else: # d1 == d2
        if (s1 < s2):
            car[s1 - 1] = 0
            car[g - 1] = 1
            s1 = g
        else:
            car[s2 - 1] = 0
            car[g - 1] = 2
            s2 = g
