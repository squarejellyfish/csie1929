s = 0.
while True:
    num = input()
    if (num == 'q'):
        break

    try:
        num = float(num)
        if (not num.is_integer()):
            s += num - num // 1
    except ValueError:
        continue

print("{:.2f}".format(s))
