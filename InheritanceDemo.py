"""
What all items we can inherit from parent class to child class:
- Attributes: Subclasses inherit all attributes (both data attributes and methods) from the parent class unless explicitly overridden.
- Methods: Subclasses inherit all methods defined in the parent class unless explicitly overridden.
- Constructor: Subclass inherits the constructor(__init__) method of the parent class unless explicitly overridden. However, the
            constructor of the parent class needs to be called explicitly within the subclass constructor if needed.
- Class Variables : Subclass inherit class variables from the parent class.
- Class methods and static methods: Subclass inherits class methods and static methods from the parent class.
"""

"""
What cannot be inherited: 
- Private member: Members with a double underscore prefix(__) are considered as private and cannot directly inherited by subclass. 
                  However, they can sometimes be accessed or modified using name mangling. 
- Special Methods: Special methods (e.g., __str__(), __repr__(), __add__() etc.) need to be explicitly overridden in the subclass
                if required. They are not inherited by default. 
- Class level attributes that are not defined in the parent class: If a class level attribute is not in the subclass that is not 
            defined in the parent class, it will not be inherited by other subclass instances of the parent class. 
            
"""
class test:
    def __init__(self,name):
        self.name = name
    def test_1(self):
        print("this is my first class")

    @staticmethod
    def static_method():
        print("This is my static method")
class child_test(test):
    pass

child_obj = child_test("Vipin")
child_obj.test_1()
print(child_obj.name)
child_obj.static_method()