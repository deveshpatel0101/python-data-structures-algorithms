class SimpleQueue:
    '''
    An implementation of Simple Queue (FIFO).
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

    def insert(self, element):
        '''
        inserts an element and raises exception if queue is overflowed
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

    def delete(self):
        '''
        deletes an element and returns it or raises exception if queue is underflowed
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

    def get_queue(self):
        '''
        returns a list of all elements
        '''
        return self.queue
