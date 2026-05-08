import pandas as pd

data = {
    "Name": ["Sarthak", "Rohit", "Harshit", "John"],
    "Age":[25, 29, 38, 45],
    "Salary" : [60000, 433344, 81000, 54500],
    "Gender": ["Male", "Female", "Male", "Male"],
}

df = pd.DataFrame(data)

print("Students whose Gender is male:- \n",df[df["Gender"] == "Male"], "\n")

print("Students whose Age is Greater than 30 :- \n", df[df["Age"] >= 30], "\n")
