class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def buy(self):
        print(f"Buying a car")

class SportCar(Car):

    def buy(self):
        print(f"Buying a sport car")

s = SportCar("BMW", 5, "2020")
s.buy()
