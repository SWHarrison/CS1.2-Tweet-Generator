from linkedlist import LinkedList

class Queue(LinkedList):

    def __init__(self):

        super(Queue, self).__init__()

    def enqueue(self, data):

        self.append(data)

    def dequeue(self):

        node_to_return = self.head
        self.delete(node_to_return.data)

    def __iter__(self):

        super(self).__iter__

    def __next__(self):

        super(self).__next__

if __name__ == "__main__":

    q = Queue()
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(5)
    q.dequeue()

    for item in q:
        print(item)
