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

item1 = 'apple'
item2 = 'banana'
item3 = 'orange'
print(item1 + ' ' + item2 + ' ' + item3) # apple banana orange

# List example
fruits = ['apple', 'banana', 'orange']
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[2]) # orange
print(fruits) # ['apple', 'banana', 'orange']
