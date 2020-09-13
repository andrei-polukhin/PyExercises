# import time
# import random
import queue

from threading import Thread  # still needed for daemon threads
from concurrent.futures import ThreadPoolExecutor

counter = 0
job_queue = queue.Queue()  # prints out
counter_queue = queue.Queue()  # increments


def increment_manager():
    global counter
    while True:
        increment = counter_queue.get()
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f"New counter value is {counter}", "--------"))
        counter_queue.task_done()


Thread(target=increment_manager, daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()


Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)


with ThreadPoolExecutor(max_workers=10) as pool:
    [pool.submit(increment_counter) for x in range(10)]

counter_queue.join()
job_queue.join()
