from collections import deque

friends = deque(("Andrew", "James", "Anna", "Amy"))


def get_friends():
    yield from friends


def greet(g):
    while True:
        try:
            yield f"Hello, {next(g)}"
        except StopIteration:
            break


friends_generator = get_friends()
g = greet(friends_generator)

print(next(g))
print(next(g))
print(next(g))
print(next(g))  # using for is prohibited as generator will become empty
