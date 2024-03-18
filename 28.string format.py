# # str.format() = optional method that gives users 
# #                more control when displaying output

# animal = "cow"
# item = "moon"

# # print("The "+animal+" jumped over the "+item)
# # print("The {} jumped over the {}".format(animal,item))
# # print("The {1} jumped over the {0}".format(animal,item)) #positional argument
# # print("The {animal} jumped over the {item}".format(animal="cat",item="moon")) #keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# name = "Farzana"

# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))   # add padding
# print("Hello, my name is {:>10}. Nice to meet you".format(name))   # right align
# print("Hello, my name is {:^10}. Nice to meet you".format(name))   # centre align

number = 1000

print("The number pi is {:.2f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:E}".format(number))  # scientific notation







