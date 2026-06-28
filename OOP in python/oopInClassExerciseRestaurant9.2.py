class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)
        print()


# Creating 3 restaurant instances
restaurant1 = Restaurant("KFC", "Fast Food")
restaurant2 = Restaurant("Pizza Hut", "Italian")
restaurant3 = Restaurant("Cafe Javas", "Cafe")

# Calling describe_restaurant() for each
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()