# 

class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display_details(self):
        super().display_details()
        print(f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}")

if __name__ == "__main__":
    Employee1 = Manager("Piyush", 1,00,00,00,000 , "CSE")
    Employee1.display_details()

