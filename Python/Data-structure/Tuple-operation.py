t1 = (1, 2, 3)
t2 = (4, 5)

print(t1 + t2)   # Output: (1, 2, 3, 4, 5)
print(t1 * 2)    # Output: (1, 2, 3, 1, 2, 3)
print(len(t1))    # Output: 3

print(2 in t1)  # Output: True
print(10 in t1) # Output: False

point1 = (1, 2)
point2 = (4, 6)

distance = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5
print(distance)  # Output: 5.0
