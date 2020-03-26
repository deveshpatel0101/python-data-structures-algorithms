class CircularDoubleEndedQueue:
    """
    An implementation of Circular Double Ended Queue (FIFO).
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

    def insertFront(self, element):
        # check for initial insertion
        if self.front == -1:
            self.front = self.rear = 0
            self.queue[self.front] = element
            return

        # reset front pointer
        if self.front == 0:
            self.front = self.size
        else:
            self.front -= 1

        # check for overflow
        if self.front == self.rear:
            if self.front == self.size:
                self.front = 0
            else:
                self.front += 1
            raise Exception('\n-- Queue Overflow --')

        # insert element
        self.queue[self.front] = element

    def insertRear(self, element):
        # check for overflow
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
            raise Exception('\n-- Queue Overflow --')

        # insert element
        self.queue[self.rear] = element

        # set front pointer
        if self.front == -1:
            self.front = 0

    def deleteFront(self):
        # check for underflow
        if self.front == -1:
            raise Exception('\n-- Queue Underflow --')

        # delete element
        element = self.queue[self.front]
        self.queue[self.front] = 'null'

        # check if queue is empty
        if self.front == self.rear:
            self.front = self.rear = -1
            return element

        # increment front pointer
        if self.front == self.size:
            self.front == 0
        else:
            self.front += 1

        return element

    def deleteRear(self):
        # check for initial condition
        if self.rear == -1:
            raise Exception('\n-- Queue Underflow --')

        # delete element
        element = self.queue[self.rear]
        self.queue[self.rear] = 'null'

        # check if queue is empty
        if self.front == self.rear:
            self.front = self.rear = -1

        # set rear pointer
        if self.rear == 0:
            self.rear = self.size
        else:
            self.rear -= 1

        return element

    def display(self):
        return self.queue
