import itertools

l = [5, 1, 2, 7]
g = itertools.dropwhile(lambda x: abs(x)>4, l)

for i in g:
	# print the first false and all after it 
	print(i)
