class Pokemon:
    __pkmCt = 0
    def __init__(self, name="No Name", lv=1, hp=1) -> None:
        if (name and not name.isspace()):
            self.__Name = name
        else:
            print("Name can't be empty.")
            self.__Name = "No Name"
        if (lv >= 1):
            self.__Lv = lv
        else:
            print("Lv setting error.")
            self.__Lv = 1
        if (hp >= 1):
            self.__HpMax = hp
        else:
            print("Hp setting error.")
            self.__HpMax = 1

        self.__HpCur = self.__HpMax
        Pokemon.__pkmCt += 1

    def ShowInfo(self):
        print("Alive Pokemon: {}".format(Pokemon.__pkmCt))
        print("Name: {}".format(self.__Name))
        print("Lv: {}".format(self.__Lv))
        print("HP: {}/{}\n".format(self.__HpCur, self.__HpMax))

    def Attack(self, target):
        if (self.__HpCur <= 0):
            print("{} is unable to attack.".format(self.__Name))
            return
        if (target.__HpCur <= 0):
            print("{} cannot attack fainted target {}.".format(self.__Name, target.__Name))
            return

        print("{} Attack {} {} Points.".format(self.__Name, target.__Name, self.__Lv))
        target.Defence(self.__Lv)

    def Defence(self, n):
        self.__HpCur -= n
        if (self.__HpCur <= 0):
            print("{} is fainted.".format(self.__Name))
            self.__HpCur = 0

    def Cure(self):
        self.__HpCur = self.__HpMax

    def __del__(self):
        print("{} has returned to the nature.".format(self.__Name))
        Pokemon.__pkmCt -= 1
