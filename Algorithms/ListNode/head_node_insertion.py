class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertHead(self, newNode):
        """
        The logic of the function is to temporarily
        store the current head node. Put the new head
        node into the beginning, and then connect to
        the temporarily stored head node.
        """
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

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
fNode = Node("Andrew")
sNode = Node("John")
tNode = Node("James")

linked_list.insertEnd(fNode)
linked_list.insertEnd(sNode)
linked_list.insertHead(tNode)

linked_list.printList()
