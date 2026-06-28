class Student:
   name="john"
   nationality="ugandan"

#  using the init constructor  
   def __init__(self, age, religion):
    self.age=age
    self.religion=religion

# instantiating the class    
student1=Student(22,"Christian")
print(student1.age)
