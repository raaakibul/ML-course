my_set = {1, 2, 3, 4, 4, 2}
print(my_set)  # Output: {1, 2, 3, 4} (Duplicates removed)

my_set.add(5)  # Add element
print(my_set)

my_set.remove(3)  # Remove element
print(my_set)

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Union: {1, 2, 3, 4, 5}
print(A & B)  # Intersection: {3}
print(A - B)  # Difference: {1, 2}
