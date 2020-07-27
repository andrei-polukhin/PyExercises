import itertools
"""
itertools.cycle
"""
rectangle = itertools.cycle("MNKP")
for i in range(78):
    print(next(rectangle))
