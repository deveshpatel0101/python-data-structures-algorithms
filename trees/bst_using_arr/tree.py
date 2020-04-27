from traversal import ArrayTreeTraversal


class Node:
    def __init__(self, data):
        self.data = data
        self.freq = 1


class BinarySearchTree:
    def __init__(self):
        self.tree = []
        for i in range(5):
            self.tree.append(None)

    def __incrementTreeSize(self, size):
        for i in range(size):
            self.tree.append(None)

        return len(self.tree) 

    def insert(self, data):
        index = 0
        while True:
            if len(self.tree) < index+1:
                self.__incrementTreeSize(index - len(self.tree)+1)

            if self.tree[index] == None:
                self.tree[index] = Node(data)
                return
            elif self.tree[index].data == data:
                self.tree[index].freq += 1
                return
            elif data < self.tree[index].data:
                index = (2*index) + 1
            elif data > self.tree[index].data:
                index = (2*index) + 2

    def search(self, data):
        return self.__searchNodeUtil(0, data)

    def __searchNodeUtil(self, index, data):
        if len(self.tree) < index+1:
            return None
        elif self.tree[index] == None:
            return None
        elif self.tree[index].data == data:
            return self.tree[index]
        elif data < self.tree[index].data:
            return self.__searchNodeUtil((2*index) + 1, data)
        elif data > self.tree[index].data:
            return self.__searchNodeUtil((2*index) + 2, data)

    def simpleDisplay(self):
        for index in range(len(self.tree)):
            if self.tree[index]:
                print(
                    f'{index}. Data: {self.tree[index].data}, Freq: {self.tree[index].freq}')
            else:
                print(f'{index}. None')

    def getTree(self):
        return self.tree

    def bfsTraversal(self):
        return ArrayTreeTraversal(self.tree).bfsTraversal()

    def dfsPreOrderTraversal(self):
        return ArrayTreeTraversal(self.tree).dfsTraversal('pre')

    def dfsInOrderTraversal(self):
        return ArrayTreeTraversal(self.tree).dfsTraversal('in')

    def dfsPostOrderTraversal(self):
        return ArrayTreeTraversal(self.tree).dfsTraversal('post')
