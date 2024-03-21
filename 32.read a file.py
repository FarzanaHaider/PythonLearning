# with open('test.txt') as file:  # will automatically close the file
#     print(file.read())

# print(file.closed)

try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")