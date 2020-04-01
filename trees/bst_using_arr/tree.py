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
                data = {
                    'found': None, 'freq': None, 'parent': None, 'sibling': None, 'leftChild': None, 'rightChild': None
                }

                if index == 0:
                    # root element
                    data['found'] = self.tree[index]
                    (leftChild, rightChild) = self.__getChildren(index)
                    data['leftChild'] = leftChild if leftChild else None
                    data['rightChild'] = rightChild if rightChild else None
                elif index % 2 != 0:
                    # found left element
                    parentIndex = int((index-1)/2)
                    (leftChild, rightChild) = self.__getChildren(index)
                    data['found'] = self.tree[index].data
                    data['freq'] = self.tree[index].freq
                    data['parent'] = self.tree[parentIndex].data
                    data['sibling'] = self.tree[(parentIndex*2)+2].data
                    data['leftChild'] = leftChild if leftChild else None
                    data['rightChild'] = rightChild if rightChild else None
                else:
                    # found right element
                    print(f'{index}')
                    parentIndex = int((index-2)/2)
                    (leftChild, rightChild) = self.__getChildren(index)
                    data['found'] = self.tree[index].data
                    data['freq'] = self.tree[index].freq
                    data['parent'] = self.tree[parentIndex].data
                    data['sibling'] = self.tree[(parentIndex*2)+1].data
                    data['leftChild'] = leftChild if leftChild else None
                    data['rightChild'] = rightChild if rightChild else None

                return data

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
