def PrintData(**Data):
    if ("uid" in Data):
        print("The user id: {}".format(Data["uid"]))
    if ("name" in Data):
        print("The username: {}".format(Data["name"]))
    if ("age" in Data):
        print("The user age: {}".format(Data["age"]))

uid, name, age = int(input()), input(), int(input())
PrintData(age=age, name=name,uid=uid)
uid, name = int(input()), input()
PrintData(name=name, uid=uid)
name = input()
PrintData(name=name)
