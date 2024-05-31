while True:
    try:
        a = eval(input(""))
        b = int(input(""))
        c = a/b
        print("{}/{} = {:.2f}".format(a, b, c))
        break
    except NameError:
        print("NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
