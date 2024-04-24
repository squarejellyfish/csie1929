txt, py = [], []
tc, pc = 1, 1
while True:
    file = input()
    if (file == "-1"): break

    name, ext = ".".join(file.split(".")[:-1]), file.split(".")[-1]
    if (ext == "txt"):
        txt.append("T{:02d}_{}.txt".format(tc, name.title())) 
        tc += 1
    elif (ext == "py"):
        py.append("P{:02d}_{}.py".format(pc, name.upper()))
        pc += 1

print(txt)
print(py)

