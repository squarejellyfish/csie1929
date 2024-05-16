def printData(**data):
    print(data['uid'])
    print(data['name'])

uid, name, age = int(input()), input(), int(input())
printData(uid=uid, name=name, age=age)
