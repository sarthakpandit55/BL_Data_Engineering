# In many applications, a "logical" error isn't necessarily a "system" error.
# The Goal: Create a custom exception class called InvalidAgeError.
# The Task: Write a function set_age(age) that:
# Raises InvalidAgeError if the age is negative or greater than 120.
# Raises a standard TypeError if the input isn't an integer.


class InvalidAgeError(Exception):
    pass

def set_age(user_age):
    try:
        if user_age > 120 or isinstance(user_age, int):
            raise InvalidAgeError("Invalid Age, Please enter a valid Age")
        print(f"{user_age} Age is valid")
    except TypeError:
        print(f"{user_age} Age is invalid")

    finally:
        print(30*"-")
        print("Program is completed")

age = int(input("Enter your age: "))
set_age(age)