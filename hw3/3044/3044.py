name = input()
grade = ['A+','A','A-','B+','B','B-','C+','C','C-','F']
grade = {g: 0 if g == 'F' else 1 for g in grade}

req, elect = 0, 0
with open(name, "r") as f:
    for i, line in enumerate(f):
        if (i == 0): continue

        line = line[:-1]
        cname, category, cred, g = line.split(",")
        if (category == "R"):
            req += grade[g] * int(cred)
        elif (category == "E"):
            elect += grade[g] * int(cred)

print("Required: {}".format(req))
print("Elective: {}".format(elect))
if (req < 72 or elect < 28):
    print("N")
    if (req < 72 and elect < 28):
        print("Student still needs to complete {} required credits & {} elective credits for graduation.".format(72 - req, 28 - elect))
    elif (req < 72):
        print("Student still needs to complete {} required credits for graduation.".format(72 - req))
    elif (elect < 28):
        print("Student still needs to complete {} elective credits for graduation.".format(28 - elect))
else:
    print("Y")

