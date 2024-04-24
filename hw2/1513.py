n = int(input())

foods, mk = {'fuck': -1}, "fuck"
for _ in range(n):
    input_s = input().split()
    food, num = input_s[0], int(input_s[1])

    if (food in foods):
        foods[food] += num
    else:
        foods[food] = num

    if (foods[food] > foods[mk]):
        mk = food

print(mk, foods[mk])
