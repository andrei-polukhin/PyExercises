"""
The `math` library gives factorial() method.
Even though, it is still useful to calculate it ourselves
"""


def factorial(n):
    # Let's apply the rule: n! = (n-1)!*n
    if n == 0:
        # Usually taken n==1, but 0!=1 anyway.
        return 1
    return factorial(n-1)*n


print("5! = ", factorial(5))  # 120
print("8! = ", factorial(8))  # 40320
print("3! = ", factorial(3))  # 6

"""
The question arises here: isn't it easier
to ``import math`` and what is faster: the math module
or our function?

To compare, let's see what `timeit` says about
``math.factorial()`` and our function:
"""

print("\nComparing the speed of the math module and our function:")
import timeit

function_setup = """def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n"""

time_math_module = timeit.timeit(
    stmt="math.factorial(31)", setup="import math"
)
time_function = timeit.timeit(
    stmt="factorial(31)", setup=function_setup
)

print("Time on our function: ", time_function, " seconds.")
print("Time on math.factorial() ", time_math_module, " seconds.")

print(
    f"\nFor 31!, <time_on_math_module>"
    f" is faster than <time_on_function> on "
    f"{time_function-time_math_module} seconds."
)
