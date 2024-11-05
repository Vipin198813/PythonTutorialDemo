class Device:
    def __init__(self,cost,manufacturer, camera):
        print("We are inside the constructor")
        self.__cost = cost      #private attribute
        self.manufacturer = manufacturer
        self.camera = camera

    # Getter function
    def show(self):
        print(self.__cost)

class mobile(Device):
    # Getter function
    def check(self):
        print(self.cost)

m = mobile(5000, "moto","dslr")
m.show()