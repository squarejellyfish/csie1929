last = -1
ans = 0
while (1):
    this = input()
    if (this == 'q'):
        break
    this = int(this)

    if (last == 1 and this == 9):
        ans += 1

    last = this

print(ans)
