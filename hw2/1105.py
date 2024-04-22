students = [[76, 73, 85],
          [88, 84, 76],
          [92, 82, 92],
          [82, 91, 85],
          [72, 74, 73],
          ]

maxi, total, m = 0, 0, 0
for num, student in enumerate(students):
    print("student " + str(num + 1))
    for i, score in enumerate(student):
        print(" {}: {}".format(i + 1, score))
    s = sum(student)
    total += s
    print(" sum: {}".format(s))
    print(" avg: {:.2f}".format(s/3))
    if (s > m):
        m = s
        maxi = num

print("total: {}, avg: {:.2f}".format(total, total / 15))
print("highest avg: student {}: {:.2f}".format(maxi + 1, m / 3))
