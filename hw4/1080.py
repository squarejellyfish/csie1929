def print_mon(mon: dict):
    print("Name: {}".format(mon["name"]))
    print("Lv: {}".format(mon["lv"]))
    print("HP: {}".format(mon["hp"]))
    print()

pokemons = []

n = int(input())

for i in range(n):
    name, lv, hp = input(), int(input()), int(input())
    pokemons.append({"name": name, "lv": lv, "hp": hp})

op = int(input())

if (op == 0):
    for mon in pokemons:
        print_mon(mon)
elif (op == 1):
    pokemons.sort(key=lambda x: x["name"])
    for mon in pokemons:
        print_mon(mon)
elif (op == 2):
    pokemons.sort(key=lambda x: x["lv"])
    for mon in pokemons:
        print_mon(mon)
elif (op == 3):
    pokemons.sort(key=lambda x: x["hp"])
    for mon in pokemons:
        print_mon(mon)
