
def main():
    x = input().split()
    n, m = int(x[0]), int(x[1])

    if (m % 2 != 0):
        print("NO")
        return

    x = (m - 2*n) / 2
    y = n - x
    if (x < 0 or y < 0):
        print("NO")
        return 

    print("YES")
    print(int(y), int(x))

main()
