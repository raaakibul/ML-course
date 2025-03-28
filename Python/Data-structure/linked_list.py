class Node:
    def __init__(self, datavalue=None):
        self.datavalue = datavalue
        self.nextvalue = None

class LinkedList:
    def __init__(self):
        self.headvalue = None
        
    def printlist(self):
        printvalue = self.headvalue
        while printvalue is not None:
            print(printvalue.datavalue)
            printvalue = printvalue.nextvalue

x = LinkedList()
x.headvalue = Node("A")
data = Node("B")
data2 = Node("C")

x.headvalue.nextvalue = data
data.nextvalue = data2
x.printlist()