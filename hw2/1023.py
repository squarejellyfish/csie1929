def argmin(a):
    return min(range(len(a)), key=lambda x : a[x])
def argmax(a):
    return max(range(len(a)), key=lambda x : a[x])

n = int(input())
nums = [int(x) for x in input().split()]

i1, i2 = argmax(nums), argmin(nums)
print(i1 + 1, nums[i1])
print(i2 + 1, nums[i2])
