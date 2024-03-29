class Stack:
    '''
    Stack is a data structure that implements LIFO/FILO
    '''

    def __init__(self, size=5):
        self.items = []
        self.size = size
        self.top = 0

    def get_size(self):
        '''
        returns the size of stack
        '''

        return self.size

    def push(self, item):
        '''
        pushes an element at the top of stack
        '''

        if self.top == self.size:
            raise Exception('\n-- Stack Overflow! --')
        self.items.append(item)
        self.top += 1
        return item, self.top

    def pop(self):
        '''
        pops an element from the top of stack and return it
        '''

        if self.top == 0:
            raise Exception('\n-- Stack underflow! --')
        self.top -= 1
        return self.items.pop(), self.top

    def is_empty(self):
        '''
        returns True if stack is empty and False otherwise
        '''

        return self.items == []

    def is_full(self):
        '''
        returns True if stack is full and False otherwise
        '''

        return len(self.items) == self.size

    def peek(self):
        '''
        returns the element that is on the top of stack
        '''

        if self.top == 0:
            raise Exception('\n-- Stack underflow! --')
        return self.items[-1]

    def get_items(self):
        '''
        returns all the elements present in the stack
        '''

        return self.items
