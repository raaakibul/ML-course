class Car:
    def __init__(self, brand, model, year):  # Constructor
        self.brand = brand   # Attribute
        self.model = model
        self.year = year

    def display_info(self):  # Method
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Creating an Object
car1 = Car("Toyota", "Corolla", 2022)
car1.display_info() # Calling a method on the object
car2 = Car("Honda", "Civic", 2021)
car2.display_info() # Calling a method on the object
# Creating a list of objects
cars = [car1, car2]
# Displaying information for each car in the list
for car in cars:
    car.display_info()  # Calling a method on each object in the list
    