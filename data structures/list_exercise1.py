# Exercise 1 (Lists)

# 1. Create a list with 5 names and output the 2nd item
names = ["Alice", "Brian", "Cathy", "David", "Esther"]
print("2nd item:", names[1])

# 2. Change the first item
names[0] = "Angela"
print(names)

# 3. Add a sixth item
names.append("Frank")
print(names)

# 4. Add "Bathel" as the 3rd item
names.insert(2, "Bathel")
print(names)

# 5. Remove the 4th item
names.pop(3)
print(names)

# 6. Negative indexing for last item
print(names[-1])

# 7. New list of 7 items, print 3rd-5th using a slice
numbers_list = ["one", "two", "three", "four", "five", "six", "seven"]
print(numbers_list[2:5])

# 8. List of countries + a copy
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
countries_copy = countries.copy()
print(countries)
print(countries_copy)

# 9. Loop through countries
for country in countries:
    print(country)

# 10. Animal list, sorted ascending and descending
animals = ["zebra", "ant", "elephant", "cat", "giraffe", "bat"]
print(sorted(animals))
print(sorted(animals, reverse=True))

# 11. Animals containing the letter 'a'
animals_with_a = [a for a in animals if "a" in a]
print(animals_with_a)

# 12. Join first names and last names lists
first_names = ["John", "Mary", "Peter"]
last_names = ["Mukasa", "Nansubuga", "Okello"]
print(first_names + last_names)