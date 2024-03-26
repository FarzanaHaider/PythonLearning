# lambda function = function written in 1 line using lamda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
#lambda parameters:expression

double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x,y: x + y
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age>=18 else False

print("After doubling: ",double(5))
print("After multiplying: ",multiply(5,6))
print("After adding: ",add(5,6))
print("Full name: ",full_name("Farzana","Haider"))
print("Age Check: ",age_check(12))