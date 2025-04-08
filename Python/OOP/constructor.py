# class object constructor attribute methods()

class Student:
    def __init__(self, name, id):
        self.name = name # instance variable
        self.id = id     # instance variable
        # print(f"Student Information: {self.name}, ID: {self.id}")
    def details(self):
        print("Name:", self.name, "ID:", self.id)
s1= Student("Bob", 101)
s2 = Student("Alice", 102)
# print(s1.name)
s1.details()
s2.details()
# print(s1.id)
# print(s2.id)
# print(s1.name, s1.id)
# print(s2.name, s2.id)

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def update_color(self, new_color):
        self.color = new_color
    
    def view(self):
        print("Dog Name:", self.name, "Color:", self.color)

dog1 = Dog("Buddy", "Brown")
dog2 = Dog("Max", "Black")
dog1.update_color("White")
dog1.view()
dog2.view()

print(dog1.__dict__)
print(dir(dog1))
        