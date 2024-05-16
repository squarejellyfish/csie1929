def fact(n):
    if (n == 0):
        return 1
    return n * fact(n - 1)

def P(n, m):
    if (m > n): return 0
    return fact(n) // fact(n - m)

def C(n, m):
    if (m > n): return 0
    return P(n, m) // fact(m)

if __name__ == "__main__":
    a = int(input())
    b = int(input())
     
    print(P(a,b))
    print(C(a,b))
