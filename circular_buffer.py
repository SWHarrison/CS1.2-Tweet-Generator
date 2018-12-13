from queue import Queue

class CircularBuffer(Queue):

    def __init__(self, max_length):

        super(CircularBuffer, self).__init__()
        self.max_length = max_length

    def enqueue(self, data):
        if(self.length_self == self.max_length):
            super().dequeue()
        self.append(data)
