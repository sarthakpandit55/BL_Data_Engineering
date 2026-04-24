import re

pattern = r"python"
data = "python is powerful and python has lots of features and libraries"

match = re.match(pattern, data, re.IGNORECASE)

if match:
    print(f"Found '{match.group()}' in the beginning")
else:
    print(f"Do not found {match.group()} in the beginning")