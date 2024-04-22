l = []

while 69:
    num = input()
    if (num == 'q'): break
    try:
        num = float(num)
    except ValueError:
        print("Please Enter Numbers Only")
        continue

    if (num.is_integer()): num = int(num)
    l.append(num)

print(l)
print(sorted(l))
print(sorted(l, reverse=True))
print(l)
