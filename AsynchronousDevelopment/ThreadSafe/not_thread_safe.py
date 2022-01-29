"""
Demonstrate the case of a not thread-safe library

We basically open each file in the read+write+append mode,
then upon several threads trying to open the file simultaneously
Python will block our attempts with
ValueError: must have exactly one of create/read/write/append mode
"""
import random
import threading

FILE_PATH = "./example.txt"


def read_file():
    contents = None
    with open(FILE_PATH, 'rw') as file:
        contents = file.read()

    return contents


def write_to_file():
    with open(FILE_PATH, 'rw') as file:
        file.write("Some random contents: " + str(random.random()))


def main():
    threads = []
    for _ in range(5):
        r_thread = threading.Thread(target=read_file, daemon=True)
        w_thread = threading.Thread(target=write_to_file, daemon=True)

        threads.append(r_thread)
        threads.append(w_thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
