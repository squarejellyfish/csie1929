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
        ret["center"] = (round((ret['S'][0] + ret['N'][0]) / 2), round((ret['E'][1] + ret['W'][1]) / 2))
        return ret
    else:
        return ret


