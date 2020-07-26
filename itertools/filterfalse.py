import itertools

l = [1, 2, 3, 4, 6]
g = itertools.filterfalse(lambda x: x<5, [1,4,6,4,1, 7])

for i in g:
	print(i)
