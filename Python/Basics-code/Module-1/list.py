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

fruits[0] = 'chips'
print(fruits)
print(fruits[:2]) # ['chips', 'banana']
print(fruits[1:]) # ['banana', 'orange']
print(fruits[-1]) # orange

fruits.append('grapes')
print(fruits) # ['chips', 'banana', 'orange', 'grapes']
fruits.insert(1, 'mango')
print(fruits) # ['chips', 'mango', 'banana', 'orange', 'grapes']
fruits.remove('banana')
print(fruits) # ['chips', 'mango', 'orange', 'grapes']

# joint two list 
food = ['pizza', 'burger', 'noodles']
print(fruits + food) # ['chips', 'mango', 'orange', 'grapes', 'pizza', 'burger', 'noodles']

items = food + fruits
print(items) # ['pizza', 'burger', 'noodles', 'chips', 'mango', 'orange', 'grapes']
print(len(items)) # 7
