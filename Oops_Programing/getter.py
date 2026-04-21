class MyClass:
    def __init__(self, name):
        self.name = name

    @property
    def get_name(self):
        return self.name

obj = MyClass("sarthak")
print(obj.get_name)
