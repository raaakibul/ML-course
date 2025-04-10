# Exception handling
x = input("Enter number1:")
y = input("Enter number2:")
try:
    z = int(x)/ int(y)
except ZeroDivisionError as e:
    print("Exception occured: ", e)
    z = None
except TypeError as e:
    print("Type error exception:")
    z = None

print("Division is: ",z)
