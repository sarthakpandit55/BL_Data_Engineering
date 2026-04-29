def divide(num1, num2):
    if num2 <= 0:
        raise ZeroDivisionError("division by zero is not possible")
    return num1/num2