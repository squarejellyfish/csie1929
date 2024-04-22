def main():
    role = int(input())

    if (role == 1):
        score = int(input())
        if (score > 100 or score < 0):
            print("score error")
            return
        print("pass" if score >= 60 else "fail")
    elif (role == 2):
        score = int(input())
        if (score > 100 or score < 0):
            print("score error")
            return
        print("pass" if score >= 70 else "fail")
    else:
        print("role error")
        return

main()
