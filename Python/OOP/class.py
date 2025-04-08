class Student:
    def __init__(self): # Constructor
        print("This is a constructor")

s1 = Student() # Creating an object of the class
print(s1) # Printing the object memory address
print(type(s1)) # Printing the type of the object
print(isinstance(s1, Student)) # Checking if s1 is an instance of Student class

# system defined variables
x = 10 # Global variable
print(x) # Printing the global variable
print(type(x)) # Printing the type of the global variable
print(isinstance(x, int)) # Checking if x is an instance of int class

