studentAge={"ariella": 12, "Alfreda":1} 
# print(studentAge.get("ariella"))
studentAge.update({"israella":4})
studentAge.update({"Alfreda":0})
print(studentAge)
# studentAge.pop("ariella")
print(studentAge) 

# getting only keys from the dictionary
namesOnly= studentAge.keys()
print(namesOnly)

# printing them individually
for nameOnly in namesOnly:
    print(nameOnly)

items =studentAge.items()
print(items)

for key, value in studentAge.items():
    print(f"{key}:{value}")
          