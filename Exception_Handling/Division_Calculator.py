# Create a simple division program that takes two inputs from a user.
# The Goal: Handle the two most common errors: ZeroDivisionError (dividing by zero) and ValueError (entering text instead of a number).
# Challenge: Use a finally block to print "Calculation attempt finished," regardless of whether the operation succeeded or failed.


def calculator():
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Please enter second division greater than Zero, Division by Zero is not possible")
    except ValueError:
        print("Please enter a number only")
    finally:
        print(30*"-")
        print("Calculation attempt finished")


a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
calculator(a, b)