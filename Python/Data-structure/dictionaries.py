my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)
print(my_dict["name"])  # Output: Alice

my_dict["age"] = 30  # Modify value
print(my_dict)

my_dict["country"] = "USA"
print(my_dict)

del my_dict["city"]
print(my_dict)
# dictioary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

numbers = {'a': 10, 'b': 15, 'c': 20, 'd': 25}
even_numbers = {k: v for k, v in numbers.items() if v % 2 == 0}

print(even_numbers)  # Output: {'a': 10, 'c': 20}

text = "hello hello world python world"
word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # Output: {'hello': 2, 'world': 2, 'python': 1}
