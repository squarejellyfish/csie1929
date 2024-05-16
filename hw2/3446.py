k, w = map(int, input().split())

projects, capitals, profits = [], [], []
while True:
    op = input()
    if (op == "-1"):
        break
    elif (op == "-2"):
        print("project:", sorted(projects))
        print("capital:", [x for _, x in sorted(zip(projects, capitals))])
        print("profits:", [x for _, x in sorted(zip(projects, profits))])
    elif (op == "-3"):
        output = [(name, cap, pro) for name, cap, pro in zip(projects, capitals, profits)]
        output.sort(key=lambda x: (-(x[2] - x[1]), x[0]))
        c, real = 0, []
        for r in output:
            if (r[1] <= k and c < w):
                real.append(r)
                c += 1
        for r in sorted(real):
            print(r[0])
            print("capital:", r[1])
            print("profits:", r[2])
    else:
        projects.append(op)
        cap, pro = map(int, input().split())
        capitals.append(cap)
        profits.append(pro)

