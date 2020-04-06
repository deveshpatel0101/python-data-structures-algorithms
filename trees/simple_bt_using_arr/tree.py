from traversal import ArrayTreeTraversal


class Node:
    def __init__(self, data):
        self.data = data
        self.freq = 1


class SimpleBinaryTree:
    def __init__(self):
        self.tree = []

    def __getChildren(self, index):
        leftChildIndex = (index*2)+1
        rightChildIndex = (index*2)+2
        leftChild = None
        rightChild = None

        if leftChildIndex < len(self.tree):
            leftChild = self.tree[leftChildIndex]
        if rightChildIndex < len(self.tree):
            rightChild = self.tree[rightChildIndex]

        return (leftChild, rightChild)

    def __getSibling(self, index, siblingOf):
        parentIndex = -1
        if siblingOf == 'left':
            parentIndex = int((index-1)/2)
        else:
            parentIndex = int((index-2)/2)

        if siblingOf == 'left' and (parentIndex*2)+2 < len(self.tree):
            return self.tree[(parentIndex*2)+2]
        elif siblingOf == 'right' and (parentIndex*2)+1 < len(self.tree):
            return self.tree[(parentIndex*2)+1]

        return None

    def __getNodeInfo(self, index):
        data = {'freq': None, 'parent': None, 'sibling': None,
                'leftChild': None, 'rightChild': None}
        if index == 0:
            # fount root element
            data['freq'] = self.tree[index].freq
            (leftChild, rightChild) = self.__getChildren(index)
            data['leftChild'] = leftChild.data if leftChild else None
            data['rightChild'] = rightChild.data if rightChild else None
            return data

        if index % 2 != 0:
            # found left element
            parentIndex = int((index-1)/2)
            (leftChild, rightChild) = self.__getChildren(index)
            sibling = self.__getSibling(index, 'left')
            data['freq'] = self.tree[index].freq
            data['parent'] = self.tree[parentIndex].data
            data['sibling'] = sibling.data if sibling else None
            data['leftChild'] = leftChild.data if leftChild else None
            data['rightChild'] = rightChild.data if rightChild else None
        else:
            # found right element
            parentIndex = int((index-2)/2)
            (leftChild, rightChild) = self.__getChildren(index)
            sibling = self.__getSibling(index, 'right')
            data['freq'] = self.tree[index].freq
            data['parent'] = self.tree[parentIndex].data
            data['sibling'] = sibling.data if sibling else None
            data['leftChild'] = leftChild.data if leftChild else None
            data['rightChild'] = rightChild.data if rightChild else None

        return data

    def insert(self, data):
        for node in self.tree:
            if node.data == data:
                node.freq += 1
                return

        self.tree.append(Node(data))

    def search(self, data):
        for index in range(len(self.tree)):
            if self.tree[index].data == data:
                return self.__getNodeInfo(index)

        raise Exception('\n-- Data not found --')

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
