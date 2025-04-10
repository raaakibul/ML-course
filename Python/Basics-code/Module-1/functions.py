# Defining a simple function
def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()


# Function with parameters
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function with arguments
greet("Alice", 25)
greet("Bob", 30)

# Function with a return value
def add(a, b):
    return a + b

# Using the function and storing the result
result = add(10, 20)
print("The sum is:", result)


# Function with default argument
def greet(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function with and without the second argument
greet("Alice")  # Uses the default age
greet("Bob", 30)

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))


def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())
print(greet("Bob"))

def calculate_triangle_are(base, height):
    return 1/2*(base*height)

def calculate_square_area(length):
    return length*length