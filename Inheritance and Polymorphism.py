print("========INHERITANCE=============")
class Animal:
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def bark(self):
        print("Wooff")

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()
print("===========POLYMORPHISM=============")

class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says wooff!!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says meow!!"

niko = Dog("Niko")
felix = Cat("felix")
print(niko.name)
print(niko.speak())


