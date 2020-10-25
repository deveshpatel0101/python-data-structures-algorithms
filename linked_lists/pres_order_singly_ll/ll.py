class Node:
    '''
    A node data structure holds two values:
    1. Data to store in the node
    2. A pointer to the next node
    '''

    def __init__(self, data):
        self.data = data
        self.next = None


class PreserveOrderLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        '''
        Inserts a node while preserving the order
        '''

        node = Node(data)

        if self.head == None:
            self.head = self.tail = node
            return

        currNode = self.head
        if data <= currNode.data:
            node.next = self.head
            self.head = node
            return

        while currNode.next != None:
            if currNode.data <= node.data and currNode.next.data >= node.data:
                break
            currNode = currNode.next
        if currNode.next == None:
            currNode.next = node
            self.tail = node
        else:
            temp = currNode.next
            node.next = temp
            currNode.next = node

    def shift(self):
        '''
        removes the first node and returns the data stored in it
        '''

        if self.head == None:
            raise Exception

        if self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            return data

        data = self.head.data
        self.head = self.head.next

        return data

    def removeMiddle(self, position):
        '''
        removes a node from the specified position and returns the data stored in it
        '''

        if position <= 0:
            raise Exception
        elif position == 1:
            return self.shift()
        elif self.head == None:
            raise Exception

        currNode = self.head

        for i in range(0, position-2):
            if currNode.next == self.tail:
                raise Exception
            currNode = currNode.next

        data = currNode.next.data
        if currNode.next == self.tail:
            currNode.next = None
            self.tail = currNode
        else:
            currNode.next = currNode.next.next

        return data

    def pop(self):
        '''
        removes a node from the end and returns the data stored in it
        '''

        if self.head == None:
            raise Exception

        if self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            return data

        currNode = self.head
        while currNode.next.next != None:
            currNode = currNode.next

        data = currNode.next.data
        self.tail = currNode
        self.tail.next = None
        return data

    def getPointers(self):
        '''
        returns the head and tail pointers
        '''

        return self.head, self.tail
