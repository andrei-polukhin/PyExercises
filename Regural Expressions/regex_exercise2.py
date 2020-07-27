import re

def reg(string):
    expression = "^\w+"
    if re.search(expression, string):
	    print(True)
    else:
	    print(False)


if __name__ == "__main__":
    text = input("Enter your string: ")
    reg(text)
