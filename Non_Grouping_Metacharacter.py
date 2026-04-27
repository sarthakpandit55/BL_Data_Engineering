import re

text = "Visit https://www.example.com or https://google.com"
pattern = r"https://(?:www\.)?\w+\.\w+"

print(re.findall(pattern, text))