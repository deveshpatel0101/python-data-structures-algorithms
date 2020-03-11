class Stack:
    def __init__(self):
        self.items = []
        self.size = 5
        self.top = 0

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def push(self, item):
        if self.top == self.size:
            raise Exception('\n-- Stack Overflow! --')
            return
        self.items.append(item)
        self.top += 1
        return item, self.top

    def pop(self):
        if self.top == 0:
            raise Exception('\n-- Stack underflow! --')
            return
        self.top -= 1
        return self.items.pop(), self.top

    def is_empty(self):
        return self.items == []

    def peek(self):
        if self.top == 0:
            raise Exception('\n-- Stack underflow! --')
            return
        return self.items[len(self.items)-1]

    def display(self):
        return self.items
