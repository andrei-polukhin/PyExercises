def countdown(n):
    while n > 0:
        yield n
        n -= 1


g1 = countdown(10)
g2 = countdown(20)


print(next(g1))
print(next(g2))

print(next(g1))
print(next(g2))

# Notice that multiple generators can work as threads!
# We initialize g1 and g2 - and then use them when needed.

"""This is what asynchronous Python development is based on."""
