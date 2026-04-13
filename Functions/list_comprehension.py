# increase the given list by 2 and put them in new list
x = [1,3,4,5,6,8]
new_x = [x+2 for x in x ]
print(new_x)


# find the cube of even number between the range of 1 to 11
cube = [x**3 for x in range(1,11) if x % 2 == 0]
print(cube)

# The Goal: Create a list of numbers from 1 to 50 that are divisible by both 3 and 5.
# Input: range(1, 51)
# Expected Output: [15, 30, 45]

lst = [num for num in range(1, 51) if num%3 == 0 and num%5 == 0]
print(lst)


# The Goal: Given a list of words, create a list of integers representing the length of each word, but only if the word contains the letter "e".
# Input: ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig']
# Expected Output: [5, 6, 4, 8] (Lengths of apple, cherry, date, eggplant)


fruits = ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig']
new_fruits = [len(fruit) for fruit in fruits if "e" in fruit]
print(new_fruits)


# The Goal: Given a list of integers, create a new list where even numbers are divided by 2, and odd numbers are multiplied by 10.
# Input: [1, 2, 3, 4, 5, 6]
# Expected Output: [10, 1.0, 30, 2.0, 50, 3.0]
# Hint: Use the expression if condition else expression syntax.

lst1 = [1,2,3,4,5,6]
new_lst1 = [num/2 if num%2 == 2 else num*10 for num in lst1 ]
print(new_lst1)


