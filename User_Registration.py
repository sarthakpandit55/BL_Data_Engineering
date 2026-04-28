import json
import os
import re

class UserRegistration:
    userId = 1
    pattern = r"[A-Z][a-z]"

    def __init__(self):
        self.userName = None
        self.userEmail = None
        self.__userPassword = None
        self.userId = None

    def registration(self):
        print("Welcome To Registration Page")
        print("-"*40)

        self.userName = input("Enter your username :- ")
        self.userEmail = input("Enter your email :- ")
        self.__userPassword = input("Enter your password :- ")

        if not re.match(self.__userPassword, UserRegistration.pattern):
            print("Invalid Password")
            print("^[A-Za-z].{7,}$")
            return

        self.userId = UserRegistration.userId
        UserRegistration.userId = UserRegistration.userId + 1

        registration_data = self.show_object()

        if os.path.isfile("registration.json"):
            with open("registration.json", "r") as f:
                try:
                    data = json.load(f)
                except:
                    data = []
        else:
            data = []

        data.append(registration_data)

        with open("registration.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Registration Successful")

    def show_object(self):
        return {"userId": self.userId,
                "userName": self.userName,
                "userEmail": self.userEmail,
                "userPassword": self.__userPassword
                }

    def login(self):
        print("Welcome To Login Page")
        print("-"*40)

        if not os.path.isfile("registration.json"):
            print("No User have registered yet")
            return

        email = input("Enter your email :- ")
        password = input("Enter your password :- ")

        with open("registration.json", "r") as f:
            try:
                data = json.load(f)
            except:
                print("Something went wrong")

        for user in data:
            if user["userEmail"] == email and user["userPassword"] == password:
                print("Login Successful")
                return

        print("Login Failed")


user = UserRegistration()
# user.registration(
user.login()

