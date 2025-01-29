class Car:
    def __init__(self, brand, model, year):  # Constructor
        self.brand = brand   # Attribute
        self.model = model
        self.year = year

    def display_info(self):  # Method
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Creating an Object
car1 = Car("Toyota", "Corolla", 2022)
car1.display_info()
