import re

data = "email address : sarthakpandit55@gmail.com, sarthak.pandit_cs22@gla.ac.in"

pattern = r"(\w+\.?\w+)@(\w+)\.(\w+\.?\w+)"

matches = re.findall(pattern, data)
for match in matches:
    print(f"Username: {match[0]}")
    print(f"Domainname: {match[1]}")
    print(f"Website Type: {match[2]}")
    print("-"*20)

