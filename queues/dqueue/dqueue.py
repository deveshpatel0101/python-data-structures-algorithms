class DoubleEndedQueue:
    '''
    An implementation of Double Ended Queue (FIFO).
    '''

    def __init__(self, size=4):
        self.rear = -1
        self.front = -1
        self.size = size
        self.queue = []
        for i in range(self.size+1):
            self.queue.append('null')

    def get_pointers(self):
        '''
        returns front and rear pointers
        '''
        return self.front, self.rear

    def insertFront(self, element):
        '''
        inserts an element from the front pointer and returns error if can't be inserted
        '''
        # check for initial insertion
        if self.front == -1:
            self.front = self.rear = 0
            self.queue[self.front] = element
            return

        # check if element can be inserted
        if self.front == 0:
            raise Exception('\n-- Element cannot be inserted --')

        # decrement front pointer
        self.front -= 1

        self.queue[self.front] = element

    def insertRear(self, element):
        '''
        inserts an element from the rear pointer and returns error if can't be inserted
        '''
        # check for overflow
        if self.rear >= self.size:
            raise Exception('\n-- Queue Overflow --')

        # increment rear pointer
        self.rear += 1

        self.queue[self.rear] = element

        # set front pointer
        if self.front == -1:
            self.front = 0

    def deleteFront(self):
        '''
        deletes an element from the front pointer and returns error if element can't be deleted
        '''
        # check for underflow
        if self.front == -1:
            raise Exception('\n-- Queue Underflow --')

        # delete element
        element = self.queue[self.front]
        self.queue[self.front] = 'null'

        # check if queue is empty
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            # increment front pointer
            self.front += 1

        return element

    def deleteRear(self):
        '''
        deletes an element from the rear pointer and returns error if element can't be deleted
        '''
        # check for initial condition
        if self.rear == -1:
            raise Exception('\n-- Element cannot be deleted --')

        # delete element
        element = self.queue[self.rear]
        self.queue[self.rear] = 'null'

        # check if queue is empty
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear -= 1

        return element

    def get_queue(self):
        '''
        returns a list of all elements
        '''
        return self.queue
