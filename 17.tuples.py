# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Farzana",21,"female")

print(student.count("Farzana"))
print(student.index("female"))

for x in student:
    print (x)

if "Farzana" in student:
    print("Farzana is here.")