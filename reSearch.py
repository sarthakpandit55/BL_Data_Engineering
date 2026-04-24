import re

pattern = "python"
data = "python is powerful and python has lots of features and libraries"

match = re.search(pattern, data)
if match:
    print(f"Found : {match.group()}")
else:
    print("No match found")