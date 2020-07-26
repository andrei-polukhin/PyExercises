import itertools
import string

number = int(input("Enter number of sides of your polygon: "))
all_letters = string.ascii_uppercase
needed_letters = all_letters[0:number]

perm = int(input("Enter the number of permutations: "))

g = itertools.permutations(needed_letters, perm)

print(next(g), 0)

for i in list(g):
	print(i)
