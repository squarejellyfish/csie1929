import os
import shutil

if os.path.exists("files"):
    shutil.rmtree("files")
os.mkdir("files")
os.chdir("files")

n = int(input())
for i in range(n):
    os.mkdir("f{}".format(i + 1))

print(sorted(os.listdir()))
os.rename("f1", "folder1")
print(sorted(os.listdir()))
shutil.rmtree("folder1")
print(sorted(os.listdir()))
os.chdir("..")
shutil.rmtree("files")


