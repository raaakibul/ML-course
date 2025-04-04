A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)  # Output: {1, 2} (Elements in A but not in B)
print(B - A)  # Output: {5, 6} (Elements in B but not in A)
print(A ^ B)  # Output: {1, 2, 5, 6} (Elements in A or B, but not both)
print(A | B)  # Output: {1, 2, 3, 4, 5, 6} (Elements in A or B)
print(A & B)  # Output: {3, 4} (Elements in both A and B)
print(A <= B) # Output: False (A is a subset of B)
print(A >= B) # Output: False (A is a superset of B)
print(A < B)  # Output: False (A is a proper subset of B)

items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))
print(unique_items)  # Output: [1, 2, 3, 4, 5]
