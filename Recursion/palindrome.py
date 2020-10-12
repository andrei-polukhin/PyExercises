def palindrome(string):
    if len(string) <=1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome(string[1:-1])

