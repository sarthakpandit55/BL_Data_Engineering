import pandas as pd

data = {
    "Name": ["Sarthak", "Rohit", "Harshit"],
    "Age": [21, 25, 22],
    "Marks": [95, 80, 76],
}

de = pd.DataFrame(data)
print(f"Original DataFrame :-\n {de}\n")


# Targeting Column
print(f"Targeted DataFrame:- \n {de["Name"]}\n")

# Targeting Multiple Columns
print(f"Targeted DataFrame:- \n {de[["Name", "Marks"]]}\n ")
