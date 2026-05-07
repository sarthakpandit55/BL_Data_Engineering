import pandas as pd

data = {
    "Name": ["Sarthak", "Rohit", "Harshit"],
    "Age": [21, 25, 22],
    "Marks": [95, 80, 76],
}

de = pd.DataFrame(data, columns=["Name", "Age", "Marks"])
print(de)

# printing specific columns
print(de[["Name","Marks"]])
