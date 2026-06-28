class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def info(self):
     print(f"Name: {self.name}, Breed: {self.breed}")

class Dog(Animal):
   def Sound(self):
      print(self.name, "Barks")


w=Dog("Tommy", "Bulldog")
w.info()
w.Sound()
