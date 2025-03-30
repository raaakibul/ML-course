# Creating a list with different data types
my_list = [1, 2, 3, "Hello", 4.5]

print(my_list)  # Output: [1, 2, 3, "Hello", 4.5]

print(my_list[0])   # First element: 1
print(my_list[-1])  # Last element: 4.5

my_list.append(10)  # Adds at the end
print(my_list)

my_list.insert(2, 200)  # Insert 200 at index 2
print(my_list)

my_list.pop()   # Removes last element
print(my_list)

my_list.remove(200)  # Removes first occurrence of 200
print(my_list)
