from traversal import ArrayTreeTraversal


class Node:
    def __init__(self, data):
        self.data = data
        self.freq = 1


class SimpleBinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, data):
        for node in self.tree:
            if node.data == data:
                node.freq += 1
                return

        self.tree.append(Node(data))

    def search(self, data):
        for index in range(len(self.tree)):
            if self.tree[index].data == data:
                return self.tree[index]

        return None

    def simpleDisplay(self):
        for index in range(len(self.tree)):
            print(
                f'{index}. Data: {self.tree[index].data}, Freq: {self.tree[index].freq}')

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
