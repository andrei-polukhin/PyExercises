import re


def reg(string):
    expression = "a(0|b+)"
    matches = re.search(expression, string)
    if matches.group(0) == string:
        print(True)
    return False


if __name__ == "__main__":
    text = input("Enter your string: ")
    reg(text)
