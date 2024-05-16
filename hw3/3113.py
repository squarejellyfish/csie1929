def add(*nums):
    return sum(nums)

lst = [int(input()) for _ in range(3)]
print(add(*lst))
lst = [int(input()) for _ in range(2)]
print(add(*lst))
