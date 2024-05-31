from func import flame_breathing
m = int(input())
s1, s2 = input().split()
s1, s2 = int(s1), int(s2)
 
train = [0 for _ in range(m)]
train[s1 - 1], train[s2 - 1] = 1, 2
print(train)
 
num_lst = [int(i) for i in input().split()]
final_train = flame_breathing(train, *num_lst)
print(final_train)
