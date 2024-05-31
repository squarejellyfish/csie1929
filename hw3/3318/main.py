from decimal import Decimal, ROUND_HALF_UP

def BD_Construction(MatrixA, District):
    count = 0
    ret = {'N': (1024, 1024), 'S': (-1, -1), 'W': (1024, 1024), 'E': (-1, -1), 'district': District}
    for x, row in enumerate(MatrixA):
        for y, num in enumerate(row):
            if (num == 1): 
                count += 1
                if (x < ret["N"][0]):
                    ret["N"] = (x, y)
                if (y < ret["W"][1]):
                    ret["W"] = (x, y)
                if (x >= ret["S"][0]):
                    ret["S"] = (x, y)
                if (y >= ret["E"][1]):
                    ret["E"] = (x, y)


    if (count <= 9):
        return {'N': None, 'S': None, 'W': None, 'E': None, 'center': None, 'district': District}
    elif (count >= 15):
        x, y = ret['S'][0] + ret['N'][0], ret['E'][1] + ret['W'][1]
        if (x % 2 == 0):
            x //= 2
        else:
            x = (x + 1) // 2
        if (y % 2 == 0):
            y //= 2
        else:
            y = (y + 1) // 2

        ret["center"] = (x, y)
        return ret
    else:
        return ret

def main():
    input_mat = []

    while True:
        row = input()
        if (row.isalpha()):
            break

        row = [int(x) for x in row.split()]
        input_mat.append(row)

    result = BD_Construction(input_mat, row)
    if (not result["N"]):
        print(None)
        return

    print("District-{}".format(row))
    print("N({},{})".format(*result["N"]))
    print("S({},{})".format(*result["S"]))
    print("W({},{})".format(*result["W"]))
    print("E({},{})".format(*result["E"]))
    if ("center" in result):
        print("Command center({},{})".format(*result["center"]))

main()
