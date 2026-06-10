class car:
    def __init__(self,brand,color,horsepower,fuel_type):
        self.brand = brand
        self.color = color
        self.horsepower = horsepower
        self.fuel_type = fuel_type
    
    def drive(self):
        print(f"The {self.color} {self.brand} is now driving")
    
    def car_info(self):
        print(f"{self.brand} {self.color} {self.horsepower}")
    
    def fuel_info(self):
        print(f"{self.fuel_type}")

if __name__ == "__main__":
    car1 = car("Toyota", "Red", 1200, "Petrol")
    
    car2 = car("Honda", "Blue", 1250, "Diesel")
    
    car3 = car("BMW", "Black", 1300, "Electric")

    print(car1.brand)
    car1.drive()
    car2.fuel_info()
    car3.car_info()
    