from math import sqrt

score = float(input())

print("Original: {:.2f}".format(score))
print("Adjusted: {:.2f}(+{:.0f})".format(sqrt(score) * 10, sqrt(score)*10 - score))
