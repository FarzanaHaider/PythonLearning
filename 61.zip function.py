# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired with paired elements stored in tuples for each element.

usernames = ["Dude","Bro","Mister"]
passwords = ("paasword","abc123", "guest")
login_date = ["1/1/2024","1/2/2024","1/3/2024"]

# users = zip(usernames, passwords) 
# users = list(zip(usernames, passwords))
# for i in users:
#     print(i)


# users = dict(zip(usernames, passwords))

# print(type(users))

# for key,value in users.items():
#     print(key+" : "+value)

users = zip(usernames,passwords,login_date)

for i in users:
    print(i)