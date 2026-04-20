# Task: Given a list of numbers, create a dictionary where each number is a key and its cube is the value.
# Input: numbers = [1, 2, 3, 4]
# Goal: {1: 1, 2: 8, 3: 27, 4: 64}
from jedi.plugins.django import mapping

num = [1,2,3,4]
d = {key : key**3 for key in num}
print(d)

# Task: Given a list of words, create a dictionary where the word is the key and its length is the value.
# Input: words = ["MERN", "Python", "API"]
# Goal: {'MERN': 4, 'Python': 6, 'API': 3}


words = ["MERN", "Python", "API"]
new_word = {key : len(key) for key in words}
print(new_word)

# Task: Given a dictionary of student scores, create a new dictionary containing only those who scored 75 or above.
# Input: results = {'Sarthak': 88, 'Rahul': 65, 'Dhwani': 92, 'Amit': 70}
# Goal: {'Sarthak': 88, 'Dhwani': 92}

results = {'Sarthak': 88, 'Rahul': 65, 'Dhwani': 92, 'Amit': 70}
new_result = {key: value for key, value in results.items() if value > 75}
print(new_result)

# Task: Given a range of numbers from 1 to 10, create a dictionary of even numbers as keys and the string "Even" as the value.
# Input: range(1, 11)
# Goal: {2: 'Even', 4: 'Even', 6: 'Even', 8: 'Even', 10: 'Even'}

even = {key : "Even" for key in range(1,11) if key % 2 == 0}
print(even)


# Task: Invert a dictionary so that the old values become the new keys and the old keys become the new values.
# Input: mapping = {'A': 1, 'B': 2, 'C': 3}
# Goal: {1: 'A', 2: 'B', 3: 'C'}

m = {'A':1, "B":2, "C":3}
new_m = {value : key for key, value in m.items()}
print(new_m)


# Task: Given two lists (one of keys and one of values), combine them into a single dictionary.
# Input: keys = ['id', 'status', 'role'], values = [101, 'active', 'admin']
# Goal: {'id': 101, 'status': 'active', 'role': 'admin'}


keys = ['id', 'status', 'role']
values = [101, 'active', 'admin']

dictio = {k:v for k, v in zip(keys, values)}
print(dictio)


# Task: Given a list of temperatures in Celsius, create a dictionary where the temperature is the key and the value is "Warm" if it's above 25, otherwise "Cold".
# Input: temps = [15, 30, 22, 28]
# Goal: {15: 'Cold', 30: 'Warm', 22: 'Cold', 28: 'Warm'}


temp = [15, 30, 22, 28]
new_temp = {key : "Cold" if key < 25  else "Warm" for key in temp}
print(new_temp)

