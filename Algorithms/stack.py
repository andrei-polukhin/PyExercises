class Stack:
    def __init__(self):
        # Initializing an empty list
        self.items = []

    def push(self, e):
        # Adding a new element to the end
        # of the list
        self.items = self.items + [e]

    def pop(self):
        # Removing and returning the last element
        # from the list
        return self.items.pop()
