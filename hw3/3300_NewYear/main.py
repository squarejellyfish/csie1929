from collections import OrderedDict
am = input()

amount = open("./Amounts/{}".format(am), "r").read()
amount = sum([int(x) for x in amount.split()])

ing = input()
ing = open("./Ingredients/{}".format(ing), "r").readlines()

amount_table = OrderedDict()
for i in ing:
    i = i.split()
    name, each = i[0], int(i[1])
    amount_table[name] = each * amount

writer = open("./Ingredients.txt", "w")
output = ["{} {}\n".format(name, val) for name, val in amount_table.items()]
writer.writelines(output)

for line in output:
    print(line, end="")

