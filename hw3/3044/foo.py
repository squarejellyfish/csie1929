with open("fuck.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        print(line)
