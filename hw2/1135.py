from math import ceil

n = int(input())

nums = [int(x) for x in input().split()]

if (n % 2 == 1):
    print(nums[n // 2])
else:
    print(ceil((nums[n // 2] + nums[n // 2 - 1]) / 2))
