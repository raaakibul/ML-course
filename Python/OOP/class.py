class Student:
    def __init__(self,name, id, age): # Constructor
        print("This is a constructor")
        self.name = name
        self.id = id
        self.age = age
        print(f"Name: {name}, ID: {id}, Age: {age}")

s1 = Student("John", 101, 23)
s2 = Student("Doe", 102, 34)