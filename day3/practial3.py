#what is dictionary
dict = {"name":"Rohit","Roll":200,"percentage":90.20}
print(dict)

print(dict["Roll"])

print(dict.get("name"))

for key in dict:
    print(key)

for key in dict:
    print(key,"=",dict[key])

#add subjects and its name in dictionary in above dictionary
dict["subjects"] = ["Maths","Science","English"]
print(dict)

#add new element in dictonary 
dict.update({"country": "India"})
print (dict)
#delete items from dictionary usign pop function
dict.pop("subjects")
print(dict)

#delete items from dictionary using del keyword
del dict["country"]
print(dict)

#empty dictionary 
dict.clear()
print(dict)

#create nested dictionary
dict1 = {"name":"rohit","roll":200}
dict2 = {"subject":["Maths","science"]}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

#print simple string and reverse
str = "Rohit Patil "
print(str[::-1])

# add "java" in above string
str = str + "java"
print (str)

#string concatination
str = "hello World"
str1 = "java"

str2  = str + " " + str1
print(str2)

print(str.casefold())
print(str.capitalize())
print(str.center(60))
print(str.upper())
print(str.endswith("world"))
print(str.endswith("World"))
print(str.startswith("hello"))
print(str.index("World"))

str3 = "12344"
print(str3.isalnum())
print(str3.isdecimal())

str4 = "Rohit123"
print(str4.isalpha())

str5 = "Rohit123"
print(str5.isidentifier())

str6 = "  "
print(str6.isspace())

str7 = "ROhit"
str8 = "paTIL"
print(str7.swapcase())
print(str8.swapcase())

str9 = "    Python"
print(str9.strip(), "programming")
print(str9.center(60), "programming")
print(str9.lstrip(), "programming")
print(str9.rstrip(), "programming")

str10 = ("i love java")
print("original string:", str10)
str=str10.replace("java", "python")
print("updated string:", str)


