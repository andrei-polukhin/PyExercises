"""
Syntax for list slicing:
    list[start:stop:step]
"""
l1 = [1, 2, 3, 4, 5]
print(l1[1:-1:2])  # start from second, till the end, step=2

l2 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
print(l2[::3])  # usual, but with step=3

l3 = [-6, -3, 0, 3, 6, 9]
print(l3[:4:])  # usual, but stop before 5th element

l4 = [-4, -2, 0, 2, 4]
print(l4[2::])  # usual, but start at 3rd element

l5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
named_slice = slice(None, 3)  # stop before 4th element
print(l5[named_slice])
