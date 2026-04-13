def is_even(num):
    """
    this function is used to check if the number is even or odd.
    Input: an integer
    Output: Even or Odd
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(4))
print(is_even.__doc__)