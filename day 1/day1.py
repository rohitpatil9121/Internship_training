wt = int(input("Enter weight: "))

if 0 < wt < 2000:
    print("15 min")

elif 2000 < wt < 4000:
    print("25 min")

elif 4000 < wt < 7500:
    print("35 min")

elif wt > 7500:
    print("OVERWEIGHT")

else:
    print("Invalid weight")


a = 10
b = 12
c = 1

if (a + b >= c) and (a + c >= b) and (b + c >= a):
    print("Valid Triangle")
else:
    print("Not a Triangle")



for num in range (10,50):
    if num > 1:
        for i in range (2,num):
            if (num % i) == 0:
                is_prime = False
                break
    if is_prime:
        print(num)