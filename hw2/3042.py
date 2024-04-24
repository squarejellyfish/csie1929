words = []
alpha = "abcdefghijklmnopqrstuvwxyz"

while True:
    word = input()
    if (word == '-1'):
        break

    new = ""
    for c in word:
        if (c.isalpha()):
            new += alpha[(ord(c.lower()) - 100) % 26]
        else: new += c
    words.append(new)

print(*words, sep=" ")
