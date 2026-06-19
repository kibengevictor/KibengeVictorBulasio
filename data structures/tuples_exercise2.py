# Exercise 2 (Tuples)

# 1. Output favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
print(x[0])

# 2. Negative indexing for 2nd last item
print(x[-2])

# 3. Update "iphone" to "itel" (tuples are immutable, so convert to list first)
x = list(x)
x[1] = "itel"
x = tuple(x)
print(x)

# 4. Add "Huawei" to the tuple (convert to list, append, convert back)
x = list(x)
x.append("Huawei")
x = tuple(x)
print(x)

# 5. Loop through the tuple
for phone in x:
    print(phone)

# 6. Remove the first item (convert to list, remove, convert back)
x = list(x)
x.pop(0)
x = tuple(x)
print(x)

# 7. Create a tuple of Ugandan cities using tuple() constructor
cities = tuple(["Kampala", "Gulu", "Mbarara", "Jinja", "Mbale"])
print(cities)

# 8. Unpack the tuple
c1, c2, c3, c4, c5 = cities
print(c1, c2, c3, c4, c5)

# 9. Print 2nd, 3rd and 4th cities using a slice
print(cities[1:4])

# 10. Join two tuples of names
first_names = ("John", "Mary", "Peter")
last_names = ("Mukasa", "Nansubuga", "Okello")
print(first_names + last_names)

# 11. Tuple of colors multiplied by 3
colors = ("red", "green", "blue")
print(colors * 3)

# 12. Count occurrences of 8
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))