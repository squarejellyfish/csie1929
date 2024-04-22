itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"} # 這是第一個集合
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"} # 這是第二個集合

fruit1 = input()
fruit2 = input()

itemsA.remove("蘋果")
itemsA.add(fruit1)
itemsA.add(fruit2)

fruit1 = input()
fruit2 = input()

itemsB.remove("蓮霧")
itemsB.add(fruit1)
itemsB.add(fruit2)

iA = sorted(list(itemsA))
iB = sorted(list(itemsB))

print("iA:", iA)
print("iB:", iB)
print("union:", sorted(list(itemsA.union(itemsB))))
print("intersection:", sorted(list(itemsA.intersection(itemsB))))
adb = sorted(list(itemsA.difference(itemsB)))
bda = sorted(list(itemsB.difference(itemsA)))
print("A diff B:", adb)
print("B diff A:", bda)
new = adb + bda
print("A xor B:", sorted(new))
