a = float(input())
b = float(input())
operation = input()

if (operation == '+'):
    print("{:.2f} + {:.2f} = {:.2f}".format(a, b, a + b))
elif (operation == '-'):
    print("{:.2f} - {:.2f} = {:.2f}".format(a, b, a - b))
elif (operation == '*'):
    print("{:.2f} * {:.2f} = {:.2f}".format(a, b, a * b))
elif (operation == '/'):
    print("{:.2f} / {:.2f} = {:.2f}".format(a, b, a / b))
