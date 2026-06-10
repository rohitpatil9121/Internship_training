#sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print (set1)
set1.add(6)
print (set1)
set1.update([7, 8, 9])
print (set1)
set1.remove(3)
print (set1)

if 4 in set1:
    print("4 is in set1")   
else: 
      print("4 is not in set1")

set4 = set1.union(set2)
print(set4)

set2 = set1.copy()
print(set2)

