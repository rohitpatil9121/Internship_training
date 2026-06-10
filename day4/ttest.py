# def show(name, age):
#     print(f"Name: {name} age: {age}")

# show(age= 20, name= "Rohit")


# # def show(name, age):
# #     print(f"Name: {name},age: {age}")

# # show(name= "Rohit", age= 20 , city= "Pune")


# def show (name, age=21):
#     print(f"Name: {name} age: {age}")

# show(name= "Rohitt", age=20)


# def show (name, age=21):
#     print(f"Name: {name} age: {age}")

# name = input("Enter name: ")
# age_input =(input("Enter age: "))

# if age_input:
#     show(name=name, age= age_input)
# else:
#     show(name =name)    

# def add (*args):
#     print(type(args))
#     z = args[0],args[1],args[2]
#     print("addition:", z, args[3] )

# add(5,2,4, "Rohit")


# def add(**args):
#     print(type(args))
#     z= args['a'] + args['b'] + args['c']
#     print("addition:", z)

# add(a=6, b=5, c=7)

a= 50
def show():
    x = 20
    print("local variable:", x)
    print(a)
show()


print(" Global variavle A:", a)
