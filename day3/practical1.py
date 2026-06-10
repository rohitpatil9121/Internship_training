#add two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2.append(list1)
print(list2)

list3 = list1 + list2
print(list3)

#add two sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)

#convert string to set
string = "Rohit Patil"
set4 = set(string)
print(set4)
 
#iterate through a set
a = set("Rohit Patil")
for i in a.__iter__():
    print(i)