class House:
    def __init__(self):
        self.windows = 4 #instance variable
        self.doors = 2   #instance variable
        
    def view(self):
        print(self.windows,"Windows", self.doors, "Doors")

h1 = House()
h1.view()  
h2 = House()
h2.windows = 6
h2.view()

class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.wheels = 4 #instance variable
        
    def view(self): ## instance method
        print(self.name, self.model, "Wheels", self.wheels)
        
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("BMW", "X5")

car1.view()
car2.view()       
car3.view()