a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
n = int(input())
ans = [0, 0, 0, 0]

def dist(a: list, b: list):
    ret = (a[0] - b[0])**2 + (a[1] - b[1])**2
    return ret

for i in range(n):
    curr = [int(x) for x in input().split()]
    if (dist(curr, a) <= a[2]**2 and dist(curr, b) <= b[2]**2):
        ans[0] += 1
    elif (dist(curr, a) <= a[2]**2):
        ans[1] += 1
    elif (dist(curr, b) <= b[2]**2):
        ans[2] += 1
    else:
        ans[3] += 1

for x in ans:
    print(x)
