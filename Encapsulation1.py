class car:
    def __init__(self,year,make,model,speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = speed
    def set_speed(self,speed):
        self.__speed = 0 if speed<0 else speed

    def get_speed(self):
         return self.__speed




c = car(2021,"Toyata", "Toyota1", 12)
# print(c.get_speed())
print(c.get_speed())
c.set_speed(30)
print(c.get_speed())


