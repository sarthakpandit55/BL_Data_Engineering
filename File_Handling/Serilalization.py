import json
l = [1,2,3,4,5]

with open("serilalization.json", "w") as f:
    json.dump(l,f)


# here we are writing the dictionary into json format
d = {
    "name" : "Sarthak",
    "age" : 21,
    "gender" : "male"
}

with open("serilalization2.json", "w") as fa:
    json.dump(d, fa, indent = 4)