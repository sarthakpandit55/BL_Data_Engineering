import re

pattern = "python"
data = "python is powerful and python has lots of features and libraries"

match =  re.finditer(pattern, data, re.IGNORECASE)
print(match)

for m in match:
    print(m)