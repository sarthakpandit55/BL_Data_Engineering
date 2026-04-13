a = lambda x,y : x + y

print(a(3,3))


l = ["apple", "banana", "cherry", "mango"]
c = map((lambda s : "Yes" if s.startswith("a") else "No",l))
print(c)