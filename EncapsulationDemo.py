"""
Encapsulation in python is a key concept in OOPS that refer to the bundling of data(attributes) and methods(functions) into to single
unit called as class.
Encapsulation enforces data hiding by restricting direct access to some component of objects and providing controlled
access through methods.

Key Components of Encapsulation:
1) Data hiding - Encapsulation hides the internal representation of an object from the outside world. This ensures that an object's
                data cannot be altered in unexpected or harmful way.
2) Access Control - Encapsulation allows control over how data is accessed and modified. You can make attribute private(not accessible
        outside the class) and provide public methods to control how these private attributes are accessed or modified."""

#Components of Encapsulation in Python
#Public Attributes and Methods:
#    Public attributes and methods are accessible from outside the class.
#    In Python, attributes and methods are public by default.

class Car:
    def __init__(self, brand, speed):
        self.brand = brand  # Public attribute
        self.speed = speed  # Public attribute

    def accelerate(self):
        return f"The car is accelerating at {self.speed} km/h"

my_car = Car("Toyota", 120)
print(my_car.brand)  # Accessible from outside the class
print(my_car.accelerate())  # Public method accessible

"""
2. Protected Attributes and Methods:
Protected attributes are indicated by a single underscore _ before the attribute name.
By convention, protected attributes should not be accessed outside the class or its subclasses, but Python does not strictly enforce this.
They are intended to be used only within the class and its subclasses.
"""
class Car:
    def __init__(self, brand, speed):
        self._brand = brand  # Protected attribute
        self._speed = speed  # Protected attribute

    def _internal_method(self):  # Protected method
        return f"Processing speed: {self._speed} km/h"

class SportsCar(Car):
    def boost(self):
        return f"Boosting {self._brand} speed to {self._speed + 50} km/h"

my_sports_car = SportsCar("Ferrari", 150)
print(my_sports_car.boost())  # Accessing protected attributes in subclass

"""
3. Private Attributes and Methods:
Private attributes and methods are prefixed with two underscores (__).
These are not accessible directly from outside the class, providing a higher level of encapsulation.
Python uses name mangling to make the variable inaccessible from outside the class by renaming it to _ClassName__attributeName.
"""
class Car:
    def __init__(self, brand, speed):
        self.__brand = brand  # Private attribute
        self.__speed = speed  # Private attribute

    def __private_method(self):  # Private method
        return f"Processing brand: {self.__brand}"

    def get_speed(self):  # Public method to access private attribute
        return f"Speed is {self.__speed} km/h"

my_car = Car("Toyota", 120)
print(my_car.get_speed())  # Accessing private attribute via public method
# print(my_car.__speed)  # This will raise AttributeError

