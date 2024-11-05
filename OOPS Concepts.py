mylist = [1,2,4]
myset = {1,2,3}
#myset.add(1)
print(myset)
print(type(myset))
print(type(mylist))

class Dog():
    species = "Mammal"
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    # OPERATIONS / Actions ----> Methods
    def bark(self):
        print("WOOFSSS!!!")

my_dog = Dog(breed = "Desi Breed", name = "Tommy", spots = False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
my_dog.bark()

class Circle():

    pi = 3.14
    def __int__(self, rad = 1):
        self.rad = rad
        return rad

    def get_circumference(self):
        return self.rad * self.pi * 2

my_circle = Circle()
Pi_Value = my_circle.pi
print(Pi_Value)

Pi_radius = Circle.__int__(Circle,10)
print(Pi_radius)

Pi_Cirumference1= my_circle.get_circumference()

print(Pi_Cirumference1)
