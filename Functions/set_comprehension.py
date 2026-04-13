menu = ["pizza", "dosa", "idle", "banana shake", "sandwich", "burger", "dosa", "banana shake"]

unique_menu = {item for item in menu if "shake" in item}

print(unique_menu)

# Given a string of text, create a set containing all the unique vowels present in the string, regardless of case.
# Input: "Python Programming is Awesome"
# Goal: Output should be {'a', 'e', 'i', 'o'} (order may vary).


text = "Python Programming id Awesome"
vowels = {char.lower() for char in text if char.lower() in "aeiou"}
print(vowels)

# Given a list of integers, generate a set containing the squares of all the even numbers in the list.
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Goal: Output should be {4, 16, 36, 64, 100}

num = [1,2,3,4,5,6,7,8,9,10]
sqr = {i*i for i in num if i%2==0}
print(sqr)

# Given a list of words, create a set of the lengths of those words, but only for words that are longer than 3 characters.
# Input: ["apple", "is", "banana", "hi", "cherry", "dog"]
# Goal: Output should be {5, 6}

str1 = ["apple", "is", "banana", "hi", "cherry", "dog"]
str1_count = {len(item) for item in str1 if len(item) > 3 }
print(str1_count)


# You have a list of usernames that might have inconsistent capitalization. Create a set that contains all names in lowercase to ensure there are no duplicates like "Admin" and "admin".
# Input: ["Alice", "bob", "ALICE", "Charlie", "BOB", "dave"]
# Goal: Output should be {'alice', 'bob', 'charlie', 'dave'}

string = ["Alice", "bob", "ALICE", "Charlie", "BOB", "dave"]
unique_string = {sti.lower() for sti in string}
print(unique_string)