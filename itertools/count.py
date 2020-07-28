import itertools
"""
itertools.count
"""
g = itertools.count(start=3, step=4)
k = 1
for i in g:
    if k <= 10:
        print(i)
        k += 1
    else:
        break
