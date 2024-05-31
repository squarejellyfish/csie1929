class cls:
    def __init__(self, students) -> None:
        self.student_lst = list()
        self.student_lst.extend(students)

    def groupA(self):
        ret = sorted(self.student_lst, key=lambda x: x[0])
        self.output(ret)
        self.student_lst = ret

    def groupB(self, idx):
        ret = sorted(self.student_lst, key=lambda x: x[idx])
        self.output(ret)
        self.student_lst = ret

    def groupC(self, *idx):
        # ret = sorted(self.student_lst, key=lambda x: [x[i] for i in idx])
        for i in idx:
            self.student_lst.sort(key=lambda x: x[i])
        self.output(self.student_lst)

    def output(self, lst):
        n = len(lst) // 3
        A, B, C = [lst[i:i + n] for i in range(0, len(lst), n)]

        print("Group A:", A)
        print("Group B:", B)
        print("Group C:", C)

    def show(self):
        print(self.student_lst)
