ip = input()

if (ip.isdigit()):
    print('"{}" is a digital string.'.format(ip))
elif (ip.isspace()):
    print('"{}" is a string that all the characters are whitespaces.'.format(ip))
elif (any(not c.isalnum() for c in ip)): # contains special char
    if (any(c.isalpha() for c in ip)): # if it has any alphabet
        if (ip.upper() == ip):
            print('"{}" is a uppercase string.'.format(ip))
            print('swap to lowercase string "{}".'.format(ip.lower()))
        elif (ip.lower() == ip):
            print('"{}" is a lowercase string.'.format(ip))
            print('swap to uppercase string "{}".'.format(ip.upper()))
        else:
            print('"{}" is a normal string.'.format(ip))
    else: 
        print('"{}" is a normal string.'.format(ip))
else: # isalnum
    if (ip.isalpha()):
        if (ip.upper() == ip):
            print('"{}" is a uppercase string.'.format(ip))
            print('swap to lowercase string "{}".'.format(ip.lower()))
        elif (ip.lower() == ip):
            print('"{}" is a lowercase string.'.format(ip))
            print('swap to uppercase string "{}".'.format(ip.upper()))
        else:
            print('"{}" is an alphabet string.'.format(ip))
    else:
        print('"{}" is an alphanumeric string.'.format(ip))
