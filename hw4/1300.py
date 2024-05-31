class Emp:
    def __init__(self, ai, bi, ci):
        self.ai = ai
        self.bi = bi
        self.ci = ci
        self.dead = 0

    def attack(self, target):
        if target.ci < self.bi and self.ai > target.ai and not target.dead:
            target.dead = 1
            return 1
        return 0

emps = []
ans = 1

def attack(s, n):
    global ans
    starter = emps[s]
    for i in range(n):
        if i == s:
            continue
        if starter.attack(emps[i]):
            ans += 1
            attack(i, n)

def main():
    global ans
    n = int(input())
    for _ in range(n):
        ai, bi, ci = map(int, input().split())
        emps.append(Emp(ai, bi, ci))
    s = int(input()) - 1

    attack(s, n)

    print(ans)

main()

