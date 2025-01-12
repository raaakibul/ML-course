numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)

# List Comprehension with Conditions
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

#  Nested List Comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [x for row in matrix for x in row]
print(flattened)