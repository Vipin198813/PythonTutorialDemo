# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(self.name)
#         print(self.age)
#
# per = person("Vipin", 35)

"""Attributes:
    - Instance Attribute: Unique to each instance of the class. Defined inside the constructor.
    - Class Attribute: Shared by all the instances of the class. Defined directly inside the call and outside any method.
"""
# class Car:
#     wheels = 4  # Class attribute (same for all objects)
#
#     def __init__(self, model, color):
#         self.model = model  # Instance attribute (unique to each object)
#         self.color = color  # Instance attribute
#
# # Create two instances of the Car class
# car1 = Car("Tesla Model 3", "Red")
# car2 = Car("Ford Mustang", "Blue")
#
# # Accessing instance attributes
# print(car1.model)  # Output: Tesla Model 3
# print(car2.model)  # Output: Ford Mustang
#
# # Accessing class attribute
# print(car1.wheels)  # Output: 4
# print(car2.wheels)  # Output: 4


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name: {self.name}, age: {self.age})"

# Creating an object
p = Person("Alice", 30)
print(p)  # Output: Person(name: Alice, age: 30)


