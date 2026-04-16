string = input("enter the str : ")

char = string.split(" ")

lst = []

for i in char:
    cap = i.capitalize()
    lst.append(cap)

sentence = " ".join(lst)
print(sentence)

