class People:
    def __init__(self, birth, id, protected, infected) -> None:
        self.birth = birth
        self.id = id
        self.protected = protected
        self.infected = infected

    def infect(self):
        if (not self.protected):
            self.infected = True

inf_pow = int(input())

l = list()
while True:
    foo = input()
    if (foo == "q"):
        break

    foo = foo.split(", ")
    id, birth, order, age, protected = foo
    protected = 1 if protected == "Y" else 0
    l.append(People(birth, id, protected, False))

infected = input().split()

left = 0
for p in l:
    if (p.id in infected):
        p.infect()
        left = inf_pow
    elif (left):
        p.infect()
        left -= 1

print(infected)
for p in l:
    print(p.id, p.protected, p.infected)
