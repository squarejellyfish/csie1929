def main():
    score = int(input())
    if (score < 0 or score > 100):
        return
    if (score >= 95):
        print("獎金 2000 元")
    elif (score >= 90):
        print("獎金 1000 元")
    elif (score >= 80):
        print("獎金 500 元")
    else:
        print("獎金 0 元")

main()


