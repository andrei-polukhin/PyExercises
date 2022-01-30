"""
Demonstrate the case of a not thread-safe library

We basically open each file in the read+write+append mode,
then upon several threads trying to open the file simultaneously
we will get an empty file in the end...
"""
import random
import threading

FILE_PATH = "./example.txt"


def read_file():
    contents = None
    with open(FILE_PATH, 'r') as file:
        contents = file.read()

    return contents


def write_to_file():
    with open(FILE_PATH, 'w') as file:
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


if __name__ == '__main__':
    main()
