# Sometimes we try to grab data that just isn't there yet.
# The Task: Create a list of 3 favorite movies. Ask the user to input a number (index) to pick a movie from the list (e.g., 0, 1, or 2).
# The Goal: Handle the IndexError that happens if the user enters a number like 5 or 10.
# Challenge: Combine this with a ValueError check in case the user types "banana" instead of a number.

def grab_data():
    lst = ["Iron Man", "Spiderman", "Hulk"]
    user_input = int(input("Please enter the movie number"))
    try:
        print(lst[user_input])
    except IndexError:
        print("Please enter the index number on the basis of list")
    except ValueError:
        print("Please enter the integer value on the basis of list")
    finally:
        print(40*"=")
        print("Process Completed")

grab_data()