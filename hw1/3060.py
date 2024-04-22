nums = []

while (1):
    num = int(input())
    if (num == -1):
        break
    nums.append(num)

s = sum(nums)
print(s)
print("{:.1f}".format(s / len(nums)))
print(max(nums))
print(nums.index(max(nums)) + 1)
print(min(nums))
print(nums.index(min(nums)) + 1)

