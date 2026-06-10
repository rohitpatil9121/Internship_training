# def safe_divide(numerator, denominator):
#     try:
#         result= numerator / denominator
#         print(f"Result;{result}")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")

# safe_divide(10, 2)
# safe_divide(10, 0)


# def get_age():
#     try:
#         age_input =input("Enter age: ")
#         age = int(age_input)
#         print(f"Age: {age}")
#     except ValueError:
#         print("Invalid input")
# get_age()

def get_user_role(user_id):
    user_roles = {"admin": "rohit ", "user": "piyush", "guest11": "darshan"}
    try:
        role = user_roles[user_id]
        print(f"User role: {role}")
    except KeyError:
        print(f"warning: user id {user_id} not found")
    except Exception as e:
        print(f"Error: {e}")

get_user_role("user")
get_user_role("guest")

