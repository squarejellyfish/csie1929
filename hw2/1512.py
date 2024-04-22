n, k = map(int, input().split())
lakes = [int(x) for x in input().split()]

total = 0
for lake in lakes:
    if (lake >= k):
        total += lake - (lake % k)

print(total)
