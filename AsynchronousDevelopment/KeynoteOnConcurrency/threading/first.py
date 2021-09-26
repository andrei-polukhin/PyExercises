import random
import time
import threading
import queue


def non_locked():
    """This is a sh*tty usage, VERY error-prone"""
    counter = 0

    def worker():
        'My job is to increment the counter and print the current count'
        nonlocal counter

        counter += 1
        print('The count is %d' % counter)
        print('---------------')


    print('Starting up')
    for _ in range(10):
        threading.Thread(target=worker).start()
    print('Finishing up')


def non_locked_proof():
    """Proof of a lousy multi-threading usage for above - fussying"""
    counter = 0

    def worker():
        'My job is to increment the counter and print the current count'
        nonlocal counter

        time.sleep(random.random())  # my benevolent fuzzying :)
        counter += 1
        time.sleep(random.random())
        print('The count is %d' % counter)
        time.sleep(random.random())
        print('---------------')


    print('Starting up')
    for _ in range(10):
        threading.Thread(target=worker).start()
    print('Finishing up')


def locked_fixed_locks():
    """My fixed example of multi-threading using locks"""
    counter = 0
    threads = []
    printer_lock = threading.Lock()
    adding_lock = threading.Lock()

    def worker():
        'My job is to increment the counter and print the current count'
        nonlocal counter

        with adding_lock:
            time.sleep(random.random())  # my benevolent fuzzying :)
            counter += 1

            with printer_lock:
                time.sleep(random.random())
                print('The count is %d' % counter)
                time.sleep(random.random())
                print('---------------')

    with printer_lock:
        print('Starting up')

    for _ in range(10):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread: threading.Thread
        thread.join()

    with printer_lock:
        print('Finishing up')


def locked_fixed_queues():
    """My fixed example of multi-threading using queue"""
    counter = 0
    q = queue.Queue()

    def worker():
        'My job is to increment the counter and print the current count'

        while True:
            # q.get()
            nonlocal counter

            time.sleep(random.random())  # my benevolent fuzzying :)
            counter += 1
            time.sleep(random.random())
            print('The count is %d' % counter)
            time.sleep(random.random())
            print('---------------')
            time.sleep(random.random())
            q.task_done()


    print('Starting up')
    threading.Thread(target=worker, daemon=True).start()  # daemon kwarg is vital

    for i in range(10):
        q.put(i)

    q.join()
    print('Finishing up')


if __name__ == '__main__':
    print("------NON CAUGHT--------")
    non_locked()
    time.sleep(5)
    print("\n------GOTCHA!!------")
    non_locked_proof()
    time.sleep(5)
    print("\n------FIXED WITH LOCKS!!------")
    locked_fixed_locks()
    print("\n------FIXED WITH QUEUES!!------")
    locked_fixed_queues()
