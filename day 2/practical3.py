#convert list to string 
my_list = ['H', 'e', 'l', 'l', 'o',' ','R','o','h','i','t','!']
my_string = ''.join(my_list)
print(my_string)

#by using map function
my_list = [1, 2, 3, 4, 5, ' ', 'Rohit']
my_string = ''.join(map(str, my_list))
print(my_string)