import itertools

text = input('Enter your string: ')

for k, g in itertools.groupby(text):
	print(k, " -> ", "".join(list(g)))
