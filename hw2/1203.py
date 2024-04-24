n = int(input())

ans = [0, 0, 0]
for _ in range(n):
    this = input()

    if (this.upper() == this):
        ans[1] += 1
    elif (this.lower() == this):
        ans[0] += 1
    else:
        ans[2] += 1

print(*ans, sep=" ")
