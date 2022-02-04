"""
Demonstrate the case of a not thread-safe library

We basically open each file in the write mode,
then upon several threads trying to open the file simultaneously
we will get the corrupted file.
"""
import random
import threading


class Writer:
    """Implement NOT a thread-safe writing"""
    def __init__(self, *args):
        self.writer = open(*args)
    
    def write(self, data):
        """Write to file"""
        self.writer.write(data)
    
    def close(self):
        """
        Close the file
        """
        self.writer.close()


def test():
    """Use case"""
    FILE_PATH = "./example.txt"
    writer = Writer(FILE_PATH, "w")

    threads = []
    for _ in range(10):
        thread = threading.Thread(
            target=writer.write, args=(str(random.random()),), daemon=True
        )
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    writer.close()


if __name__ == '__main__':
    test()
