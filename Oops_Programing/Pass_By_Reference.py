class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def greet(data):
    print(f"Hi, My name is {data.name} and my age is {data.age}")


p = Person("Sarthak", 21)
greet(p)