class Node:
    '''
    A node data structure holds two values:
    1. Data to store in the node
    2. A pointer to the next node
    '''

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def unshift(self, data):
        '''
        Inserts a node at the start
        '''
        node = Node(data)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insertMiddle(self, position, data):
        '''
        Inserts a node at a given position
        '''
        if self.head == None and position > 1:
            raise Exception('\n-- Index out of range --')
        elif position == 1:
            self.unshift(data)
            return

        node = Node(data)
        currNode = self.head

        for i in range(0, position-2):
            if currNode == self.tail:
                raise Exception('\n-- Index out of range --')
            currNode = currNode.next

        if currNode == self.tail:
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
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def shift(self):
        '''
        Deletes the first node and returns the data stored in it
        '''
        if self.head == None or self.tail == None:
            raise Exception('\n-- List is empty --')

        node = self.head
        self.head = self.head.next

        if self.head == None:
            self.tail = None

        return node.data

    def deleteMiddle(self, position):
        '''
        Deletes a node from the specified position and returns the data stored in it
        '''
        if self.head == None and position > 1:
            raise Exception('\n-- Index out of range --')
        elif self.head == None or position == 1:
            return self.shift()

        currNode = self.head

        for i in range(0, position-2):
            if currNode.next == self.tail:
                raise Exception('\n-- Index out of range --')
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
        Deletes a node from the end and returns the data stored in it
        '''
        if self.head == None:
            raise Exception('\n-- List is empty --')

        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
            return node.data

        while node.next.next != None:
            node = node.next

        data = node.next.data
        self.tail = node
        self.tail.next = None
        return data

    def reverse(self):
        '''
        reverses the linked list
        '''
        if self.head == None:
            raise Exception('\n-- List is empty --')
        nxt = prev = None
        curr = self.head
        tail = self.head
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev
        self.tail = tail
        self.tail.next = None

    def getPointers(self):
        '''
        returns the head and tail pointers
        '''
        return self.head, self.tail
