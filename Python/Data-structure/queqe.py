from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # Output: deque([1, 2, 3])

queue.popleft()  # Removes first element (1)
print(queue)  # Output: deque([2, 3])
