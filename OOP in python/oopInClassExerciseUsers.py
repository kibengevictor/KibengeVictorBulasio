class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Country:", self.country)

    def greet_user(self):
        print("Hello", self.first_name + "!")
        print()


# Creating instances
user1 = User("Kibenge", "John", 22, "Uganda")
user2 = User("Sarah", "Namuli", 20, "Kenya")
user3 = User("David", "Okello", 25, "Rwanda")

# Calling methods
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()