import pandas as pd

data = {
    "Name": ["Sarthak", "Rohit", "Harshit"],
    "Age": [21, 25, 22],
    "Marks": [95, 80, 76],
}

de = pd.DataFrame(data)
de["Section"] = ["A", "B", "C"]
print(de)