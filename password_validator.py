import re

password = input("Enter your password: ")
pattern = r"[0-9A-Z]"

check = re.findall(pattern, password)

if check:
    print("Valid password")
else:
    print("Invalid password")