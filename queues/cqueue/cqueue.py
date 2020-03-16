class CircularQueue:
    """
    An implementation of Circular Queue (FIFO).
    """

    def __init__(self):
        self.rear = -1
        self.front = -1
        self.size = 4
        self.queue = []
        for i in range(self.size+1):
            self.queue.append('null')

    def get_pointers(self):
        return self.front, self.rear

    def insert(self, element):
        # reset rear pointer
        if self.rear == self.size:
            self.rear = 0
        else:
            self.rear += 1

        # check for overflow
        if self.front == self.rear:
            if self.rear == 0:
                self.rear = self.size
            else:
                self.rear -= 1
            raise Exception('\n-- Overflow --')

        self.queue[self.rear] = element

        # set front pointer
        if self.front == -1:
            self.front = 0

    def delete(self):
        # check for underflow
        if self.front == -1:
            raise Exception('\n-- Underflow --')

        # delete element
        element = self.queue[self.front]
        self.queue[self.front] = 'null'

        # check if queue is empty
        if self.front == self.rear:
            self.front = self.rear = -1
            return element

        # increment front pointer
        if self.front == self.size:
            self.front = 0
        else:
            self.front += 1

        return element

    def display(self):
        return self.queue
