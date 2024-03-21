import os

path = "test.txt"

if os.path.exists(path):
    print("The location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("Doesn;t exit")