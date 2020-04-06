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
        index = 0
        while True:
            if len(self.tree) < index+1:
                raise Exception('\n-- Data not found --')
            elif self.tree[index] == None:
                raise Exception('\n-- Data not found --')
            elif data < self.tree[index].data:
                index = (2*index) + 1
            elif data > self.tree[index].data:
                index = (2*index) + 2
            elif self.tree[index].data == data:
                found = {
                    'freq': None, 'parent': None, 'sibling': None, 'leftChild': None, 'rightChild': None
                }

                if index == 0:
                    # root element
                    found['freq'] = self.tree[index].freq
                    (leftChild, rightChild) = self.__getChildren(index)
                    found['leftChild'] = leftChild.data if leftChild else None
                    found['rightChild'] = rightChild.data if rightChild else None
                elif index % 2 != 0:
                    # found left element
                    parentIndex = int((index-1)/2)
                    (leftChild, rightChild) = self.__getChildren(index)
                    sibling = self.__getSibling(index, 'left')
                    found['freq'] = self.tree[index].freq
                    found['parent'] = self.tree[parentIndex].data
                    found['sibling'] = sibling.data if sibling else None
                    found['leftChild'] = leftChild.data if leftChild else None
                    found['rightChild'] = rightChild.data if rightChild else None
                else:
                    # found right element
                    parentIndex = int((index-2)/2)
                    (leftChild, rightChild) = self.__getChildren(index)
                    sibling = self.__getSibling(index, 'right')
                    found['freq'] = self.tree[index].freq
                    found['parent'] = self.tree[parentIndex].data
                    found['sibling'] = sibling.data if sibling else None
                    found['leftChild'] = leftChild.data if leftChild else None
                    found['rightChild'] = rightChild.data if rightChild else None

                return found

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
