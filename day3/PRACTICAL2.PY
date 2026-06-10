#take string value in tuple and perform operations
tuple1 = ("Rohit", "Patil")
print(tuple1)
tuple2 = tuple1 + ("is", "a", "student")
print(tuple2)
tuple3 = tuple1 * 2
print(tuple3)

#access value of tuple using loop
for i in tuple1:
    print(i)

for a in tuple2:
    print(a)

#join two tuples
tuple4 = tuple1 + tuple2
print(tuple4)

#get maximum and minimum value from tuple
tuple5 = (1, 2, 3, 4, 5)
print(max(tuple5))
print(min(tuple5))

#convert list into tuple
list1 = [1, 2, 3, 4, 5]
tuple6 = tuple(list1)
print(tuple6)

#how can we delete a tuple
tuple7 = (1, 2, 3, 4, 5)
del tuple7

list = list(tuple2)
del list[1]
print(list)

