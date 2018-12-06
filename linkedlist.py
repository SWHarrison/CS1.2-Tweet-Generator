class Node():

    def __init__(self, data):
        self.next = None
        self.data = data

    def update(self, new_data):
        self.data = new_data

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class LinkedList():

    def __init__(self, items = None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.iter = None
        self.length_self = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def append(self, data):
        # O(1) time as it does not depend on size of list.
        #Adds a new value, commented out chunk does not use tail of list
        '''if(self.length < 1):
            self.head = Node(data)
            self.length += 1
            return

        current = self.head

        while(current.next != None):
            current = current.next

        current.next = Node(data)
        self.length += 1'''

        new_node = Node(data)

        if(self.length_self == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length_self += 1

    def prepend(self, data):
        # O(1) time as it does not depend on size of list.

        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        self.length_self += 1

        if(self.length_self == 1):
            self.tail = self.head

    def find(self, quality):
        # O(n) time as it needs to go through the list

        '''current = self.head

        while(current != None):
            if(current.data == data):
                return current
            current = current.next

        return None'''
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def replace(self, old_data, new_data):
        # O(n) time as it needs to go through the list

        node = self.find(old_data)

        if(node != None):
            node.update(new_data)

    def find_by_index(self, index_to_find):
        # O(n) time as it needs to go through the list

        if(index_to_find > self.length_self-1):
            print("Index out of Range!")
            return None

        current = self.head
        for i in range(index_to_find):
            current = current.next

        return current

    def print_list(self):
        # O(n) time as it needs to go through the list

        print("Length: " + str(self.length_self))
        current = self.head
        while(current != None):
            print(current.data)
            current = current.next

    def length(self):
        # O(1) time as it does not depend on size of list.
        return self.length_self

    def delete(self, data):
        # O(n) time as it needs to go through the list

        #Returns error if empty list
        if(self.length_self == 0):
            raise(ValueError)

        previous = self.head
        current = previous.next

        #If head is the node to delete
        if(previous.data == data):
            if(self.length_self == 1):
                previous.next = None
                self.head = None
                self.tail = None
            else:
                previous.next = None
                self.head = current
            self.length_self -= 1
            return

        #Parses through list, and removes the node if it matches data
        while(current != None):
            if(current.data == data):
                previous.next = current.next
                current.next = None
                self.length_self -= 1
                if(current == self.tail):
                    self.tail = previous
                return

            previous = current
            current = current.next

        raise(ValueError)


    def __iter__(self):
        self.iter = self.head
        return self

    def __next__(self):
        if(self.iter != None):
            data = self.iter.data
            self.iter = self.iter.next
            return data
        else:
            raise StopIteration

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length_self))

    ll.prepend('S')

    for item in ll:
        print(item)

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'S', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length_self))


if __name__ == "__main__":
    test_linked_list()
    '''LL = LinkedList()
    LL.append(5)
    LL.prepend(3)
    LL.prepend(6)
    LL.print_list()
    LL.delete(4)
    LL.delete(6)
    LL.delete(5)
    LL.delete(3)

    print("\n\n")
    print('head: {}'.format(LL.head))
    print('tail: {}'.format(LL.tail))
    LL.print_list()

    LL.prepend(2)

    print("\n\n")
    print('head: {}'.format(LL.head))
    print('tail: {}'.format(LL.tail))
    LL.print_list()

    LL.replace(2,5)
    print("\n\n")
    print('head: {}'.format(LL.head))
    print('tail: {}'.format(LL.tail))
    LL.print_list()
    LL.append(1)

    LL.print_list()

    #print(LL.find_by_index(1).data)'''
