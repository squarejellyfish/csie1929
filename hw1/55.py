def die(x1, y1, x2, y2):
    return x1 == x2 and y1 == y2

def main():
    m,n,x1,y1,e1,n1,f1,x2,y2,e2,n2,f2 = map(int, input().split())
    t, ee1, nn1, ee2, nn2 = 0, e1, n1, e2, n2
    move_set = [[0, 1], [1, 0]] # north, east
    while (f1 or f2):
        if (f1): # robo 1
            if (nn1): # north
                x1 += move_set[0][0]
                y1 += move_set[0][1]
                nn1 -= 1
            elif (ee1): # east
                x1 += move_set[1][0]
                y1 += move_set[1][1]
                ee1 -= 1
            # trans
            if (x1 == m):
                x1 = 0
            if (y1 == n):
                y1 = 0
            if (not ee1 and not nn1):
                ee1 = e1
                nn1 = n1
            f1 -= 1
        if (f2): # robo 1
            if (ee2): # east
                x2 += move_set[1][0]
                y2 += move_set[1][1]
                ee2 -= 1
            elif (nn2): # north
                x2 += move_set[0][0]
                y2 += move_set[0][1]
                nn2 -= 1
            # trans
            if (x2 == m):
                x2 = 0
            if (y2 == n):
                y2 = 0
            if (not ee2 and not nn2):
                ee2 = e2
                nn2 = n2
            f2 -= 1
#        print(x1, y1, x2, y2)
        if (die(x1, y1, x2, y2)):
            print("robots explode at time {}".format(t + 1))
            return 
        t += 1
    print("robots will not explode")

main()
