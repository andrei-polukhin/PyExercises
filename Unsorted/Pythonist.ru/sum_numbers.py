"""
Write the function which will
find the sum of numbers from 1 to N (inclusive).

Examples:
sum_numbers(5) ➞ 15
// 1 + 2 + 3 + 4 + 5 = 15
sum_numbers(1) ➞ 1
sum_numbers(12) ➞ 78

Example solution:
https://pythonist.ru/rekursiya-summa/
"""


def sum_numbers(n):
    if n == 0:
        return 0
    return sum_numbers(n-1)+n


print(sum_numbers(5))
print(sum_numbers(1))
print(sum_numbers(12))
print(sum_numbers(0))
