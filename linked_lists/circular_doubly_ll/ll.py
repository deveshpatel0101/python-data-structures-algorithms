class Node:
    '''
    A node data structure holds two values:
    1. Data to store in the node
    2. A pointer to the next node
    3. A pointer to the previous node
    '''

    def __init__(self, data):
        self.data = data
        self.prev: Node = None
        self.next: Node = None


class CircularDoublyLinkedList:
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
            self.head.prev = self.tail
            self.head.next = self.tail
            return

        node.next = self.head
        self.head.prev = node
        self.head = node
        self.head.prev = self.tail
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
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            node.prev = currNode
            node.next = currNode.next
            currNode.next = node
            node.next.prev = node

    def push(self, data):
        '''
        Inserts a node at the end
        '''

        node = Node(data)
        if self.head == None:
            self.head = self.tail = node
            self.head.prev = self.tail
            self.tail.next = self.head
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.tail.next = self.head
        self.head.prev = self.tail

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
        self.head.prev = self.tail
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
            self.head.prev = self.tail
        else:
            currNode.next = currNode.next.next
            currNode.next.prev = currNode

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

        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail

        return data

    def reverse(self):
        '''
        reverses the linked list
        '''

        if self.head == None:
            raise Exception

        node = self.head
        while node.next != self.head:
            temp = node.prev
            node.prev = node.next
            node.next = temp
            node = node.prev
        else:
            temp = node.prev
            node.prev = node.next
            node.next = temp
            node = node.prev

        temp = self.head
        self.head = self.tail
        self.tail = temp

    def getPointers(self):
        '''
        returns the head and tail pointers
        '''

        return self.head, self.tail
