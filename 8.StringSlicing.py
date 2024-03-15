# slicing = create a substring by extracting elements from another string
#            indexing[] or slice()
#            [start:stop:step]

# name = "Farzana Haider"

# first_name = name[0:7]  #print first seven character
# last_name = name[8:15]  #name[8:]
# funky_name = name[0:15:2]
# reversed_name = name[::-1] #[0:end:-1]

# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])