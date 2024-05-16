words = ['戶頭','銀行','下單','帳號','匯','欠款','檢察官','警察','提款機','點數','發票','援交','酒店','股票','投資','顧問','課程','專員','平台']

users_score = dict()
users = []
while True:
    name = input().split()
    if name[0] == "q":
        break

    name, score = name[0], int(name[1])
    users_score[name] = score
    users.append(name)

users_count = {name: 0 for name in users}
is_cheater = {name: 1 if users_score[name] <= 3 else 0 for name in users}

while True:
    msg = input().split()
    if msg[0] == "q":
        break

    name, msg = msg[0], msg[1]
    for word in words:
        n = msg.count(word)
        users_count[name] += n
    if users_count[name] > 2:
        is_cheater[name] = 1

    if is_cheater[name]:
        print("小心詐騙!")

for name in users:
    if is_cheater[name]:
        print(name)
