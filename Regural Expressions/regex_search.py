import re

number = float(input("Enter your price: "))
print(number)
price = f"Price: ${number}"
expression = "Price: \$([0-9]*\.[0-9]*)"

matches = re.search(expression, price)

print(matches.group(0))
print(matches.group(1))
