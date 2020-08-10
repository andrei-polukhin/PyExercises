from collections import deque

friends = deque(("James", "Jose", "Evan", "John", "Daniel"))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(greeting, friend)


def greet(g):
    yield from g


greeter = greet(friend_upper())
greeter.send(None)
greeter.send("Hello,")
greeter.send("How is it going,")
