# map() = applies a function to each item in an iterable (list,tuple etc.)
#
# map (function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_taka = lambda data: (data[0],data[1]*109.63)
to_dollars = lambda data: (data[0],data[1]/109.63)

store_taka = list(map(to_taka, store))
store_dollars = list(map(to_dollars, store))

for i in store_taka:
    print(i)

for i in store_dollars:
    print(i)