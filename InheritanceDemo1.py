class Device:
    def review(self):
        print("Product is very good")

class phone(Device):
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera
        print(f"Price: {self.price}, Brand: {self.brand} , Camera: {self.camera}")

    def buy(self):
        print("Buying a new phone")

class smartphone(phone):
    pass

s = smartphone(1000,"Samsung", "12MP")
s.buy()
s.review()