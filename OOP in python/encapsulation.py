class Car:
    def __init__(self, brand, model, price):
        self.brand = brand        # public
        self._model = model       # protected
        self.__price = price      # private

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self._model)
        print("Price:", self.__price)


# Creating object
car1 = Car("Toyota", "Corolla", 50000000)

# Access public variable directly
print(car1.brand)

# Display all values using method
car1.display()