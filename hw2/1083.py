n = int(input())

words = []
m, mi = 0, 0
for i in range(n):
    words.append(input().upper())
    s = sum(ord(ch) - 64 for ch in words[i])
    if (s > m):
        m = s
        mi = i
    elif (s == m and words[i] < words[mi]):
        m = s
        mi = i
    print("{} = {}".format(words[i], s))

print("{} is the key.".format(words[mi]))

