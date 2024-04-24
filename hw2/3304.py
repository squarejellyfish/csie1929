code = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"

base = int(input())
msg = input().replace(" ", "")

new_code = "".join([code[i % 62] for i in range(base, 62 + base)])

trantab = str.maketrans(new_code, code)
msg = msg.translate(trantab)

print(msg, end='')
