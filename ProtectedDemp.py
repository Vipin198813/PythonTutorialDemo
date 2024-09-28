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
