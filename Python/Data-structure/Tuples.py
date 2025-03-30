my_tuple = (10, 20, 30, "Python")
print(my_tuple)

print(my_tuple[1])  # Output: 20
print(my_tuple[-1]) # Output: Python

a, b, c, d = my_tuple
print(a, b, c, d)  # Output: 10 20 30 Python

print(my_tuple[0:2])  # Output: (10, 20)
print(my_tuple[1:3])  # Output: (20, 30)
print(my_tuple[2:])   # Output: (30, "Python")
print(my_tuple[:3])   # Output: (10, 20, 30)
print(my_tuple[-2:])  # Output: (30, "Python")
print(my_tuple[::2])  # Output: (10, 30)
print(my_tuple[::-1]) # Output: ("Python", 30, 20, 10)
print(my_tuple[1::2]) # Output: (20, "Python")
print(my_tuple[::-2]) # Output: ("Python", 20)
print(my_tuple[1:-1]) # Output: (20, 30)
print(my_tuple[1:-2]) # Output: (20)
