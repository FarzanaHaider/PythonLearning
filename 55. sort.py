# sort() method = used with lists
# sort() function = used with iterables

# students = ["Sima","Sandy","Fara","Sara","Bro"]

# # students.sort(reverse=True)   # sort method
# sorted_students = sorted(students,reverse=True) # sort function

# for i in sorted_students:
#     print(i)

# students = [("Squid","F",60),      # list of tuples
#             ("Sandy","A",33),
#             ("Patrick","D",36),
#             ("Sponge","B",20),
#             ("Krabs","C",78)]

# # students.sort()  # sorted according to 1st column

# grade = lambda grades:grades[1]  # sort according to 2nd column
# students.sort(key=grade,reverse=True)

# for i in students:
#     print(i)

students = (("Squid","F",60),      # tuple of tuples
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Sponge","B",20),
            ("Krabs","C",78))

age = lambda ages:ages[2]
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)