class User:
    def __init__(self):
        self.name = "sarthak"

    def login(self):
        print(f"{self.name} is logged in")


class Student(User):
    def enrolled(self):
        print("Enrolled successfully into the course")

s = Student()
s.login()
s.enrolled()
print(s.name)