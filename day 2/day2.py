#Check if a number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a positive number")
if num < 0:
    print(num, "is a negative number")
if num == 0:   
    print(num, "is zero")

#Check if a number is even or odd
num = int(input("Enter a number: "))    
if num % 2 == 0:
    print(num, "is an even number")
else:    
    print(num, "is an odd number") 

#check the grade of a student based on marks
marks = int(input("Enter marks of subject 1: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

#find the largest of three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)

#FACTORIAL OF AN NUMBER using for loop 
num = (input("Enter a number: "))
fc = 1
for i in range(1, num + 1):
    fc *= i;
    i+= 1;
print("The factorial of", num, "is", fc)

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print("Original list:", my_list)
print("Reversed list:", reversed_list)
