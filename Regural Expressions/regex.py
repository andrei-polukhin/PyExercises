import re

email = "andrewmathematics2003@gmail.com"
expression = "[a-z]+"

matches = re.findall(expression, email)
print(matches)
