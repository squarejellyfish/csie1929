import Pokemon
 
name = input().strip()
lv = int(input())
hp = int(input())
p1 = Pokemon.Pokemon(name,lv,hp)
 
name = input().strip()
lv = int(input())
hp = int(input())
p2 = Pokemon.Pokemon(name,lv,hp)
 
p1.ShowInfo()
p2.ShowInfo()
 
p1.Attack(p2)
p2.Attack(p1)
p1.Attack(p2)
p2.Attack(p1)
 
p1.ShowInfo()
p2.ShowInfo()
 
#以下為測試是否將成員設成private(non-public)
private_tester = p1._Pokemon__Name
private_tester = p1._Pokemon__Lv
private_tester = p1._Pokemon__HpCur
private_tester = p1._Pokemon__HpMax
 
private_tester = p2._Pokemon__Name
private_tester = p2._Pokemon__Lv
private_tester = p2._Pokemon__HpCur
private_tester = p2._Pokemon__HpMax
