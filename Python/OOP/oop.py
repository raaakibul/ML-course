# Defining a class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute
        self.model = model  # Attribute
        self.year = year    # Attribute

    def display_info(self):  # Method
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Creating objects
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model S", 2023)

# Accessing attributes and calling methods
car1.display_info()  # Car: Toyota Corolla, Year: 2022
car2.display_info()  # Car: Tesla Model S, Year: 2023

class Car:
    wheels = 4  # Class variable (shared by all instances)

    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model

# Creating objects
car1 = Car("BMW", "X5")
car2 = Car("Audi", "A4")

print(car1.wheels)  # 4 (shared)
print(car2.wheels)  # 4 (shared)

Car.wheels = 6
