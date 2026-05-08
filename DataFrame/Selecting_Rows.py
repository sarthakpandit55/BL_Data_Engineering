import pandas as pd

data = {
    "Name": ["Sarthak", "Rohit", "Harshit"],
    "Age": [21, 25, 22],
    "Marks": [95, 80, 76],
}

de = pd.DataFrame(data)
print(de)

print(f"selecting the row 0 :-\n {de.loc[[0,1]]}")

print(f"Selecting the row and column :- \n {de.loc[[0,2]][["Name", "Marks"]]}")