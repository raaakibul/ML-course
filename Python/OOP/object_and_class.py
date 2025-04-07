class Fish:
    def __init__(self, name):
        self.name = name  # instance variable
    
    def method_print(self):
        print("Fish name:", self.name)

f1 = Fish("Goldfish")
f2 = Fish("Betta")
f1.method_print()
f2.method_print()