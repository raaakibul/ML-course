stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)

print(stack)  # Output: [1, 2, 3]

stack.pop()  # Removes last element (3)
print(stack)  # Output: [1, 2]

print(stack[-1])  # Peek (Top element: 2)
print(stack)  # Output: [1, 2]
stack.pop()  # Removes last element (2)
print(stack)  # Output: [1]
stack.pop()  # Removes last element (1)
print(stack)  # Output: []
stack.pop()  # Raises IndexError: pop from empty list
print(stack[-1])  # Raises IndexError: list index out of range
print(stack)  # Output: []
stack.pop()  # Raises IndexError: pop from empty list
print(stack[-1])  # Raises IndexError: list index out of range
print(stack)  # Output: []