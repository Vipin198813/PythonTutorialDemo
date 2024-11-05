class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an Animal")
    def eat(self):
        print("I am eating")
my_animal = Animal()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog and I am an animal")
my_dog = Dog()
my_dog.eat()

