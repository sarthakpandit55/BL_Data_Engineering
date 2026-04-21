class Student:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        """this method return the name of the student and the name is private variable"""
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 3:
            self.__name = name
        else:
            raise ValueError("Name cannot be shorter than 3 characters")


obj = Student("Sarthak")
print(obj.name)
obj.name = "Sandesh"
print(obj.name)