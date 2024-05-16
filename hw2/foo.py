# k是最高資金；w是計畫數
k = input().split()
k, w = int(k[0]), int(k[1])
projects = []
capitals = []  # 所需資金名
profits = []  # 報酬名

while True:
    name = input()
    if name == "-1":
        break
    elif name == "-2":
        print("project: {}".format(sorted(projects)))
        print("capital: {}".format([c for _, c in sorted(zip(projects, capitals))]))
        print("profits: {}".format([pro for _, pro in sorted(zip(projects, profits))]))
    elif name == "-3":
        rank = [[p, c, pro] for p, c, pro in zip(projects, capitals, profits)]
        rank.sort(key=lambda x: (-(x[2] - x[1]), x[0]))
        output, c = [], 0
        for r in rank: # 符合條件的前w個
            if (r[1] <= k and c < w):
                output.append(r)
                c += 1
        output.sort()

        for o in output:
            print(o[0])
            print("capital:", o[1])
            print("profits:", o[2])
    else:
        c = input().split()
        c, p = int(c[0]), int(c[1]) # cap, pro
        projects.append(name)
        capitals.append(c)
        profits.append(p)

