class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # insert at start
    def unshift(self, data):
        node = Node(data)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    # insert at middle
    def insertMiddle(self, num, data):
        if self.head == None and num > 1:
            raise Exception('\n-- Index out of range --')
        elif self.head == None or num == 1:
            self.unshift(data)
        else:
            node = Node(data)
            currNode = self.head

            for i in range(0, num-2):
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

    # insert at end
    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # delete from start
    def shift(self):
        if self.head == None or self.tail == None:
            raise Exception('\n-- List is empty --')

        node = self.head
        self.head = self.head.next

        if self.head == None:
            self.tail = None

        return node.data

    # delete from middle
    def deleteMiddle(self, num):
        if self.head == None and num > 1:
            raise Exception('\n-- Index out of range --')
        elif self.head == None or num == 1:
            return self.shift()
        else:
            currNode = self.head

            for i in range(0, num-2):
                if currNode.next == self.tail:
                    raise Exception('\n-- Index out of range --')
                currNode = currNode.next
            data = None
            data = currNode.next.data
            if currNode.next == self.tail:
                currNode.next = None
                self.tail = currNode
            else:
                currNode.next = currNode.next.next

            return data

    # delete from end
    def pop(self):
        if self.head == None or self.tail == None:
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
        if self.head == None:
            raise Exception('\n-- Nothing in the list to reverse --')
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

    def display(self):
        return self.head, self.tail