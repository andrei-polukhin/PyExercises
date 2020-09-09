class Queue:
    def __init__(self):
        # Initializing an empty list
        self.items = []

    def push(self, e):
        # Adding an element
        # to the end of the queue
        self.items.append(e)

    def pop(self):
        # The first elements gets returned
        # and removed from the queue
        head = self.items[0]
        self.items = self.items[1:]
        return head
