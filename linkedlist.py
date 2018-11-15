class Node():

    def __init__(value):
        self.next = None
        self.value = value

    def update(new_value):
        self.value = new_value

class LinkedList():

    def __init__(value):
        self.root = Node(value)
        self.length = 1

    def append(value):

        current = self.root

        while(current.next != None):
            current = current.next

        current.next = Node(value)
        self.length += 1

    def prepend(value):

        new_root = Node(value)
        new_root.next = self.root
        self.root = new_root
        self.length += 1

    def find(value):

        current = self.root

        while(current != None):
            if(current.value == value):
                return
