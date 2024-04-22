triangle = input().split()

res = [[],[],[],[]]
while triangle[0] != "-1":
    name = triangle[0]
    a, b, c = int(triangle[1]), int(triangle[2]), int(triangle[3])
    if (a > c): a, c = c, a
    if (b > c): b, c = c, b

    if (a + b <= c or b + c <= a or a + c <= b): res[0].append(name)
    elif (a*a + b*b > c*c): res[1].append(name)
    elif (a*a + b*b < c*c): res[2].append(name)
    elif (a*a + b*b == c*c): res[3].append(name)
    triangle = input().split()

print("Not Triangle: ", end="")
if res[0]: print(*sorted(res[0]), sep=",")
else: print(None)
print("Acute Angle: ", end="")
if res[1]: print(*sorted(res[1]), sep=",")
else: print(None)
print("Obtuse Angle: ", end="")
if res[2]: print(*sorted(res[2]), sep=",")
else: print(None)
print("Right Angle: ", end="")
if res[3]: print(*sorted(res[3]), sep=",")
else: print(None)
