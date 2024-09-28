"""
Overriding in Python is a concept in object-oriented programming where a subclass provides a specific implementation for a
method that is already defined in its superclass (parent class). The method in the subclass will override the method from the superclass,
allowing the subclass to have customized behavior for that method.

Key Points about Overriding:
Same Method Name: The method in the subclass must have the same name as the one in the superclass.
Same Parameters: The method in the subclass should have the same parameters (signature) as in the superclass.
Custom Implementation: The overridden method can have a different implementation that suits the needs of the subclass.

"""

class phone:
    def __init__(self, price, brand, camera):
        print("Inside the constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("buying a new phone]")

class smartPhone(phone):
    def buy(self):
        print("buying a new smartphone")

s = smartPhone(5000,"Samsung","20MP")
s.buy()