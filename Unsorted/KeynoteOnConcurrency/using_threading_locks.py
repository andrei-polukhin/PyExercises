import threading
import time
import random

counter_lock = threading.Lock()
printer_lock = threading.Lock()

counter = 0


def worker():
    'My job is to increment the counter and print the current count'
    global counter
    with counter_lock:
        counter += 1
        with printer_lock:
            print('The count is %d' % counter)
            print('---------------')


with printer_lock:
    print('Starting up')

worker_threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    worker_threads.append(t)
    t.start()

for t in worker_threads:
    # As soon as all threads are run, we need to wait them to end
    # SEQUENTIALLY! Interestingly, this programme has a problem:
    # using those locks, we just overcomplexified our initial programme!
    t.join()

with printer_lock:
    print('Finishing up')
