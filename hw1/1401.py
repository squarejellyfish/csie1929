i, f = 1, 1
while (1):
    n = input()
    if (n == 'q'):
        break

    if ('.' in n):
        f *= float(n)
    else:
        i *= int(n)

print("{:.2f}".format(f))
print("{}".format(i))
if (i > f):
    print("Float < Int")
elif (f > i):
    print("Float > Int")
else:
    print("Float = Int")
