my_list = [1, 2, 4, "A", 5,"B", "C", 3, "D", "E"]
my_list.append("f")
print( my_list)
my_list.insert(2, "X")
print( my_list)
my_list.remove("A")
print( my_list)
my_list.pop(3)
print( my_list)
my_list.clear()
print( my_list)

l1= [1, 2, 4,3,5,3,24,5,3]
l1.sort()
print( l1)
l1.reverse()
print( l1)

new_list= l1.copy()
print( new_list)

#min and max of a list
print( min(l1))
print( max(l1))

my_list.extend(l1)
print( my_list)

