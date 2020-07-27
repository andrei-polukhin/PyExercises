"""
This function shows how easily you can find out
the number of vowels in a word using inversion.
"""


def vowels(string, n=0):
    if not string:
        return n
    if string[0].lower() in "aeiou":
        n += 1
    return vowels(string[1:], n=n)


print(vowels("Apple"))  # 2
print(vowels("cheesecake"))  # 5
print(vowels("ccc"))  # 0
print(vowels(""))  # 0
