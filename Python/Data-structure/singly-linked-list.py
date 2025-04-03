class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # First node of the list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node  # Append at the end

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")  # Indicating end of the list

# Usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None
