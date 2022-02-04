"""
Demonstrate the case of a thread-safe library

We basically open each file in the write mode,
but we use locks so that several threads will not break the logics.
"""
import random
import threading
from queue import Queue, Empty


class Writer:
    """Implement thread-safe writing"""
    def __init__(self, *args):
        self.writer = open(*args)
        self.queue = Queue()
        self.finished = False
        threading.Thread(target=self.internal_writer, daemon=True).start()
    
    def write(self, data):
        """Put to queue"""
        self.queue.put(data)
    
    def internal_writer(self):
        """
        Provision the entered data into queue and insert into file one by one
        """
        while not self.finished:
            try:
                data = self.queue.get(timeout=1)
            except Empty:
                continue    
            self.writer.write(data)
            self.queue.task_done()
    
    def close(self):
        """
        Close the connection to writer + related queues and threads
        """
        self.queue.join()
        self.finished = True
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
