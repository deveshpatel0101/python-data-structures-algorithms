class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# implement following linked list


class PreserveOrderLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)

        # if list is empty
        if self.head == None:
            self.head = node
            self.tail = node
            return

        # if new node's value is smaller than head's value
        currNode = self.head
        if currNode.data > data:
            node.next = self.head
            self.head = node
        else:
            while currNode.next != None:
                if currNode.data < node.data and currNode.next.data > node.data:
                    break
                elif currNode.data < node.data and currNode.next.data == node.data:
                    break
                currNode = currNode.next
            if currNode.next == None:
                currNode.next = node
                self.tail = node
            else:
                temp = currNode.next
                node.next = temp
                currNode.next = node

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

    def display(self):
        return self.head, self.tail
