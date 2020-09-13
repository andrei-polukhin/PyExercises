import time
import random

from threading import Thread

counter = 0


def increment():
    global counter
    # This is called 'fuzzying', in order to find
    # the problem with shared resource modifying.
    # In this case, several threads change the variable
    # 'counter' simultaneously.
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(counter)
    time.sleep(random.random())
    print("--------")


for x in range(10):
    t = Thread(target=increment)
    time.sleep(random.random())
    # This will invoke multi-threading.
    t.start()
    # To avoid the problem, we need to use: t.join()
    # This will run the next thread if the previous one
    # has terminated
