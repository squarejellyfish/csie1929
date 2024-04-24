foods = dict()

n = int(input())
for _ in range(n):
    input_str = input().split()
    food, num = input_str[0], int(input_str[1])

    if (food in foods):
        foods[food] += num # update
    else:
        foods[food] = num # append

# find max
print("key, val: ")
for key, val in foods.items():
    print(key, val)
