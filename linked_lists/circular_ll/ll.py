class Node:
    '''
    A node data structure holds two values:
    1. Data to store in the node
    2. A pointer to the next node
    '''

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def unshift(self, data):
        '''
        Inserts a node at the start
        '''

        node = Node(data)
        if self.head == None:
            node.next = node
            self.head = self.tail = node
            return

        node.next = self.head
        self.head = node
        self.tail.next = self.head

    def insertMiddle(self, position, data):
        '''
        Inserts a node at a given position
        '''

        if position <= 0:
            raise Exception
        elif position == 1:
            return self.unshift(data)
        elif self.head == None:
            raise Exception

        node = Node(data)
        currNode = self.head

        for _ in range(0, position-2):
            if currNode == self.tail:
                raise Exception
            currNode = currNode.next

        if currNode == self.tail:
            node.next = self.head
            self.tail.next = node
            self.tail = node
        else:
            temp = currNode.next
            node.next = temp
            currNode.next = node

    def push(self, data):
        '''
        Inserts a node at the end
        '''

        node = Node(data)
        if self.head == None:
            node.next = node
            self.head = self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node

    def shift(self):
        '''
        removes the first node and returns the data stored in it
        '''

        if self.head == None:
            raise Exception
        elif self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            return data

        data = self.head.data
        self.head = self.head.next

        self.tail.next = self.head
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

        for _ in range(0, position-2):
            if currNode.next == self.tail:
                raise Exception
            currNode = currNode.next

        data = currNode.next.data
        if currNode.next == self.tail:
            currNode.next = self.head
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
        while currNode.next != self.tail:
            currNode = currNode.next

        data = currNode.next.data
        currNode.next = self.head
        self.tail = currNode
        return data

    def reverse(self):
        '''
        reverses the linked list
        '''

        if self.head == None:
            raise Exception

        nxt = prev = None

        curr = self.head
        tail = self.head
        while curr.next != self.head:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        else:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev
        self.tail = tail
        self.tail.next = self.head

    def getPointers(self):
        '''
        returns the head and tail pointers
        '''

        return self.head, self.tail
