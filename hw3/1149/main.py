name = input()

with open(name, "r") as file:
    for line in file.readlines()[1:]:
        std_num = line.split(",")[0]
        ex1, ex2, ex3, ex4, hw = map(int, line.split(",")[1:])
        total = ((ex1 + ex2 + ex3 + ex4) / 4) * 0.7 + hw / 40 * 100 * 0.3
        
        if (total < 60 and hw == 40):
            total = 60

        print("{} {:.2f}".format(std_num, total))
