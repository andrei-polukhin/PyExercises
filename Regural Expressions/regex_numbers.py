import re

def numbers(string):
	expression = "[0-9]{1,3}"
	if re.search(expression, string):
		print(True)
	else:
		print(False)

if __name__ == "__main__":
	text = input("Enter your string: ")
	numbers(text)
