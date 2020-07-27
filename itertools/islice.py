import itertools

text = input("Enter your string: ")
start_index = int(input("Enter start index: "))
end_index = int(input("Enter stop index: "))
step = int(input("Enter step: "))

g = itertools.islice(text, start_index, end_index, step)

for letter in g:
    print(letter)
