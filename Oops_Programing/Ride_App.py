# The Goal: Create a system where a Trip connects a Rider and a Driver.
# Class User: Attributes name and rating.
# Class Driver (Inherits from User): Adds vehicle_type and is_available (Boolean).
# Class Rider (Inherits from User): Adds wallet_balance.
# Class Trip (Composition): * This class should take a Driver object and a Rider object as arguments in its __init__.
# Method calculate_fare(distance): Returns $distance \times 2$.
# Method start_trip(): Should change the Driver's is_available to False.

class User:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

class Driver(User):
    def __init__(self, name, rating, vehicle_type, is_available):
        super().__init__(name, rating)
        self.vehicle_type = vehicle_type
        self.is_available = is_available


class Rider(User):
    def __init__(self, name, rating, wallet_balance):
        super().__init__(name, rating)
        self.wallet_balance = wallet_balance

class Trip:
    def __init__(self, driver, rider, distance):
        self.driver = driver
        self.rider = rider
        self.distance = distance
        self.calculate_fare()

    def calculate_fare(self):
        return self.distance * 2

    @property
    def start_trip(self):
        return self.driver.is_available

    @start_trip.setter
    def start_trip(self):
        self.driver.is_available = False


driver = Driver("Sarthak", 4.5, "SUV", True)
print(driver.rating)

rider1 = Rider("Sarthak", 4.5, 30)
print(rider1.wallet_balance)

trip1 = Trip(driver, rider1, 10)
print(trip1.start_trip)