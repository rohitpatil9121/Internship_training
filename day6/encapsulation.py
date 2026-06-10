# class BankAccount:
#     def __init__(self, owner, balance, loan):
#         self.owner = owner
#         self.balance = balance
#         self.loan = loan

#     def display_balance(self):
#         print(f"owner: {self.owner} ") 
#         print(f"balance: {self.balance}  & {self.loan} loan")

# if __name__ == "__main__":
#     account = BankAccount("Rohit", 1000, "housing")

#     print(account.owner)
#     account.display_balance()

from abc import ABC, abstractmethod
class vehicle():
    @abstractmethod
    def start_engine(self):
        pass

class car(vehicle):
    def start_engine(self):
        print("car engine is started")

my_car = car()
my_car.start_engine()    
