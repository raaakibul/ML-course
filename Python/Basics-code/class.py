class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        
    def do_work(self):
        if self.occupation =="tennis player":
            print(self.name, "Plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")
    def speak(self):
        print(self.name, "says how are you?")

tom = Human("Tom Cruise", "actor")
tom.do_work()
tom.speak()