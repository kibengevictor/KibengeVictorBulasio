class Guitar:

    def __init__(self, brand, type, price):
        self.brand=brand
        self.type=type
        self.price=price

    def guitar_description(self):
        print(f"Type: {self.type}")
        print(f"Brand: {self.brand}")
        print(f"Price: ${self.price}")
        
my_guitar=Guitar("Fender", "Electric", 1500)
my_guitar.guitar_description()