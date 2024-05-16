import time

d = float(input())

t = time.gmtime(d)
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
t = time.localtime(d)
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
