import os

source = "test.txt"
destination = "D:\\pyhon\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file")
    else:
        os.replace(source,destination)
        print(source+" was moved")

except FileNotFoundError:
    print(source+"was not found")