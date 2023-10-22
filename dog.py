class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.is_sitting = False
        self.standing = False
        self.run = True
        
    def bark(self):
        print("Woof!")
        
    def sit(self):
        if self.is_sitting:
            print(f"{self.name} is already sitting!")
        else:
            self.is_sitting = True
            print(f"{self.name} sits down.")
            
    def stand(self):
        if self.is_sitting:
            self.is_sitting = False
            self.standing = True
            print(f"{self.name} stands up")
        else:
            print(f"{self.name} is already standing!.")
    
    def run(self):
        if self.standing:
            self.run = True
            print(f"{self.name} is now running")
        else:
            print("{self.name} is not standing,it must first stand up to run.")
            
    