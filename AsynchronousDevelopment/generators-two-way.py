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

for i in range(4):
    print(next(g))  # finding len = sum(1 for _ in g) is prohibited
                    # the generator will become empty
