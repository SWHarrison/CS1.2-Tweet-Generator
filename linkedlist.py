class Node():

    def __init__(self, value):
        self.next = None
        self.value = value

    def update(self, new_value):
        self.value = new_value

class LinkedList():

    def __init__(self, value):
        self.root = Node(value)
        self.length = 1

    def append(self, value):

        if(self.length < 1):
            self.root = Node(value)
            self.length += 1
            return

        current = self.root

        while(current.next != None):
            current = current.next

        current.next = Node(value)
        self.length += 1

    def prepend(self, value):

        new_root = Node(value)
        new_root.next = self.root
        self.root = new_root
        self.length += 1

    def find(self, value):

        current = self.root

        while(current != None):
            if(current.value == value):
                return current
            current = current.next

        return None

    def find_by_index(self, index_to_find):

        if(index_to_find > self.length-1):
            print("Index out of Range!")
            return None

        current = self.root
        for i in range(index_to_find):
            current = current.next

        return current

    def print_list(self):

        print("Length: " + str(self.length))
        current = self.root
        while(current != None):
            print(current.value)
            current = current.next

    def pop(self, value):

        if(self.length < 1):
            return None

        previous = self.root
        current = previous.next

        if(previous.value == value):
            previous.next = None
            self.root = current
            self.length -= 1
            return previous

        while(current != None):
            #print("current values")
            #print(previous.value)
            #print(current.value)
            if(current.value == value):
                previous.next = current.next
                current.next = None
                self.length -= 1
                return current

            previous = current
            current = current.next

        print("Value not found")
        return None


if __name__ == "__main__":
    LL = LinkedList(4)
    LL.append(5)
    LL.prepend(3)
    LL.prepend(6)
    LL.print_list()
    LL.pop(4)
    LL.pop(6)
    LL.pop(5)
    LL.pop(3)

    LL.prepend(2)

    LL.print_list()

    LL.append(1)

    LL.print_list()
