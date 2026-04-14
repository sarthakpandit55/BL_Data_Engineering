# Imagine you are building a profile lookup tool for a small database.
# The Task: Create a dictionary called user_data with a few names as keys and ages as values. Write a function that asks the user for a name and prints that user's age.
# The Goal: Handle the KeyError that occurs if the user enters a name that isn't in your dictionary.
# Challenge: Instead of letting the program crash, print a friendly message: "Sorry, that user does not exist in our records."


def database_checker(user_data):
    name = input("Please enter the name : ")

    try:
        print(f"{name}'s age is {user_data[name.lower()]}")
    except KeyError:
        print("Sorry, that user does not exists in our records.")

data = {"rahul" : 20, "saurabh" : 25, "vishal" : 22}
database_checker(data)
