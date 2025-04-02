import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)

print(heap)  # Output: [5, 10, 15] (Always keeps smallest at top)

print(heapq.heappop(heap))  # Output: 5 (Removes smallest)
