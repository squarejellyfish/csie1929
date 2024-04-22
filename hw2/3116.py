products = {
        'T': "Top",
        'H': "Hoodie",
        'B': "Backpack"
        }

while True:
    op = input()

    if (op == "-1"): break

    if (op in products):
        print(products[op])
    elif (op == "-2"):
        out = sorted([(key, val) for key, val in products.items()], key=lambda x: x[0])
        print("keys:", [x[0] for x in out])
        print("values:", [x[1] for x in out])
    elif (op == "-3"):
        target = input()
        if (target in products):
            products.pop(target)
        else:
            print("key {} does not exist, cannot delete.".format(target))
    elif (op not in products):
        print("{} does not exist. Enter a new product category:".format(op))
        new = input()
        products[op] = new
