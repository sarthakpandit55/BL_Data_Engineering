import re
pattern = re.compile("python", re.IGNORECASE)
data = "python is powerful and python has lots of features and libraries"

match = re.match(pattern, data)

if match:
    print(f"Found")
else:
    print(f"Not found")