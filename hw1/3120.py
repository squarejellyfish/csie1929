n = int(input())

r = list(reversed(range(n)))
for i in range(n):
    if (i == 0):
        space = ' '*r[i]
        print("{}{}".format(space, "/\\"))
        continue
    elif (i == 1):
        space = ' '*r[i]
        print("{}{}".format(space, "/~~\\"))
        continue

    space = ' '*r[i]
    mid = '/' + ' '*i*2 + '\\'
    print("{}{}".format(space, mid))

print("~"*n*2)
print("~"*n*2)
        
