def main():
    input_string = input().split()
    H, A, name = int(input_string[0]), int(input_string[1]), input_string[2]

    with open("history.txt", "w") as history:
        try:
            file = open("{}.txt".format(name), "r")
            content = file.readlines()
            n, soldiers = content[0], content[1:]

            success = 0
            for i, soldier in enumerate(soldiers):
                h, a = map(int, soldier.split())

                while (h > 0):
                    if (H <= 0):
                        success = 1
                        break

                    H -= a
                    if (H > 0):
                        h -= A
                    history.write("{} {} {}\n".format(i, h, H)) 

                if (success):
                    history.write("success!")
                    break
            else:
                history.write("failed:(")
        except FileNotFoundError:
            history.write("failed:(")
            return

main()
