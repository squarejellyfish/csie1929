from statistics import mean

class student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []

    def avg(self):
        if (self.grades):
            return mean(self.grades)
        return 0

    def add(self, grade):
        self.grades.append(grade)

    def fcount(self):
        return sum(grade < 60 for grade in self.grades)

    def show(self):
        print("Name: {}".format(self.name))
        print("Gender: {}".format(self.gender))
        print("Grades: {}".format(self.grades))
        print("Avg: {:.1f}".format(self.avg()))
        print("Fail Number: {}".format(self.fcount()))
        print()

def top(*students) -> student:
    ret = student("", "")
    avg = ret.avg()
    for s in students:
        if (s.avg() > avg):
            ret = s
            avg = ret.avg()

    return ret

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)
 
s1.show()
s2.show()
s3.show()
s4.show()
s5.show()
top_student = top(s1,s2,s3,s4,s5)
print("Top Student:")
top_student.show()
