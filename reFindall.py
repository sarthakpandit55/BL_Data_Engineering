import re

pattern = "dog|cat"
data = "i have a dog which is better than other dogs and my sister have cat"

match = re.findall(pattern, data, re.IGNORECASE)

if match:
    print(match)
else:
    print("Not Found")