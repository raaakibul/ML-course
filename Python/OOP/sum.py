def sum(x,y):
    return x + y

x, y = list(map(int, input("Enter two numbers separated by space: ").split()))

print(f"The sum of {x} and {y} is: {sum(x,y)}")
