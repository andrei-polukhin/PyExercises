from collections import deque
from types import coroutine

friends = deque(("James", "Jose", "Evan", "John", "Daniel"))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(greeting, friend)


async def greet(g):
    print("Starting...")
    await g
    print("Ending...")


greeter = greet(friend_upper())
greeter.send(None)
greeter.send("Hello,")
greeter.send("How is it going,")
greeter.send("Greetings,")
greeter.send("Hi,")
greeter.send("Hi,")  # raises StopIteration as the generator is empty now
