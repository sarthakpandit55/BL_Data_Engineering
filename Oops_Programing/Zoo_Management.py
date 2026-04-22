# The Goal: Manage different animals that all share some traits but behave differently.
# Base Class: Create Animal. It should have an __init__ for name and species.
# Encapsulation: Add a private attribute __hunger_level (start at 50).
# Abstraction: Add a method make_sound() but leave it empty (or use pass).
# Inheritance: Create two subclasses: Lion and Parrot.
# In Lion, override make_sound() to print "Roar!".
# In Parrot, override make_sound() to print "Polly wants a cracker!".
# Polymorphism: Create a list containing one Lion and one Parrot. Loop through the list and call .make_sound() on both.


from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.__hunger_level = 50

    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Leo")

    def make_sound(self):
        print("Roar!")

class Parrot(Animal):
    def __init__(self, name):
        super().__init__(name, "Bird")

    def make_sound(self):
        print("Polly wants a crackers!")


lst = [
    Lion("Simba"),
    Parrot("Polly")
]

for l in lst:
    l.make_sound()