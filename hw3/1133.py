name = input()

count = {
        "PISTOL": 0,
        "SMG": 0,
        "SHOTGUN": 0,
        "AR": 0,
        "SNIPER": 0,
        }
with open(name, "r") as file:
    for line in file.readlines():
        gt, fuck = line.split("-")[0], line.split("-")[1]
        count[gt] += 1

print(count["PISTOL"], count["SMG"], count["SHOTGUN"], count["AR"], count["SNIPER"])

