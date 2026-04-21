# The Problem: The Coffee Machine
# Create a CoffeeMachine class that mimics a simple brewer.
# Attributes: water_level, coffee_beans, and is_on.
# Methods: * fill_water(amount): Increases water level.
# add_beans(amount): Increases bean count.
# make_coffee(): Checks if there is enough water/beans. If yes, it "brews" (prints a message) and reduces the resources.
# The Goal: Prevent the machine from brewing if is_on is false or resources are empty.


class CoffeeMachine:

    def __init__(self, water_level, coffee_beans, is_on):
        self.__water_level = water_level
        self.__coffee_beans = coffee_beans
        self.__is_on = is_on

    @property
    def fill_water(self):
        return f"These are the water level in container{self.__water_level}"

    @fill_water.setter
    def fill_water(self, value):
        if value > 0:
            self.__water_level += value
            print(f"You added the beans by {value}.")

    @property
    def add_beans(self):
        return f"These are the coffee beans in container{self.__coffee_beans}"

    @add_beans.setter
    def add_beans(self, value):
        if value > 0:
            self.__coffee_beans += value
            print(f"You added the beans by {value}.")

    def make_coffee(self):
        if self.__is_on:
            if self.__coffee_beans > 0 and self.__water_level > 0:
                print("Your coffee is brewing.")
                self.__coffee_beans -= 1
                self.__water_level -= 1
            else:
                raise ValueError("Your coffee is not brewing.")
        else:
            raise ValueError("Please turn on the machine")


coffee = CoffeeMachine(2, 2, True)
coffee.make_coffee()
print(coffee.add_beans)
print(coffee.fill_water)