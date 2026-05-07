import pandas as pd

s1 = pd.Series(["Sarthak", "Rohit", "Harshit"])
print(s1)

# custom index
s2 = pd.Series(["Sarthak", "Rohit", "Harshit"], index=["a", "b", "c"])
print(s2)