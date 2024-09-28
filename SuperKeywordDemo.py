"""
In Python, the super() keyword is used to call a method from a parent (or superclass) in a child (or subclass) class.
It is commonly used in object-oriented programming to give a child class access to methods or properties of its
parent class without directly referring to the parent class by name.
"""
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

class student(person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age
        super().__init__("tanveer", 30)
    def displayInfo(self):
        print(self.sName,self.sAge)

obj = student("VIPIN", 35)
obj.display()
obj.displayInfo()

