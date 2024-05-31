import maximumBags as mb
 
bag = input().split(' ')
rocks = input().split(' ')
addrock = int(input())
 
bag = list(map(int, bag))
rocks = list(map(int, rocks))
 
num = mb.maximumBags(bag, rocks, addrock)
print(num)
