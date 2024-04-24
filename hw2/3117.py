while True:
    word = input()
    if (word == "-1"): break

    new = ""
    for c in word:
        if (c == "b"): new += "d"
        elif (c == 'd'): new += 'b'
        elif (c == 'p'): new += 'q'
        elif (c == 'q'): new += 'p'
        else: new += c

    print(new)
