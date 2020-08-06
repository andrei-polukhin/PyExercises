class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("The list is empty!")
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


linked_list = LinkedList()
firstNode = Node("Andrew")
linked_list.insert(firstNode)
secondNode = Node("John")
linked_list.insert(secondNode)

linked_list.printList()
