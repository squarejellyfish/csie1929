def matrixMultiPly(a, b):
    ret = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]
    for r, row in enumerate(a):
        for i in range(3):
            val = 0
            for j in range(3):
                val += row[j] * b[j][i]
            ret[r][i] = val

    return ret

a, b = [[int(x) for x in input().split()] for _ in range(3)], [[int(x) for x in input().split()] for _ in range(3)]
c = matrixMultiPly(a, b)
for row in c:
    print(row)
