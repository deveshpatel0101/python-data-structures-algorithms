from traversal import LinkedListTreeTraversal


class Node:
    def __init__(self, data):
        self.data = data
        self.freq = 1
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.tree = None

    def __getMinValueNode(self, node):
        while node.left != None:
            node = node.left
        return node

    def insert(self, data):
        node = Node(data)
        if self.tree == None:
            self.tree = node
            return

        currNode = self.tree
        while True:
            if currNode.data > node.data and currNode.left != None:
                currNode = currNode.left
            elif currNode.data > node.data and currNode.left == None:
                currNode.left = node
                return
            elif currNode.data < node.data and currNode.right != None:
                currNode = currNode.right
            elif currNode.data < node.data and currNode.right == None:
                currNode.right = node
                return
            elif currNode.data == node.data:
                currNode.freq += 1
                return

    def search(self, data):
        if self.tree == None:
            raise Exception('\n-- Data not found --')

        currNode = self.tree
        found = {'found': None, 'parent': None, 'sibling': None,
                 'leftChild': None, 'rightChild': None, 'freq': None}

        while True:
            if currNode.data > data:
                if currNode.left != None and currNode.left.data == data:
                    found['found'] = currNode.left.data
                    found['freq'] = currNode.left.freq
                    found['parent'] = currNode.data
                    found['sibling'] = currNode.right.data if currNode.right else None
                    found['leftChild'] = currNode.left.left.data if currNode.left.left else None
                    found['rightChild'] = currNode.left.right.data if currNode.left.right else None
                    return found
                elif currNode.left == None:
                    raise Exception('\n-- Data not found --')
                else:
                    currNode = currNode.left
            elif currNode.data < data:
                if currNode.right != None and currNode.right.data == data:
                    found['found'] = currNode.right
                    found['freq'] = currNode.right.freq
                    found['parent'] = currNode.data
                    found['sibling'] = currNode.left.data if currNode.left else None
                    found['leftChild'] = currNode.right.left.data if currNode.right.left else None
                    found['rightChild'] = currNode.right.right.data if currNode.right.right else None
                    return found

                elif currNode.right == None:
                    raise Exception('\n-- Data not found --')
                else:
                    currNode = currNode.right
            else:
                found['found'] = currNode.data
                found['freq'] = currNode.freq
                found['leftChild'] = currNode.left.data if currNode.left else None
                found['rightChild'] = currNode.right.data if currNode.right else None
                return found

    def delete(self, data):
        if self.tree == None:
            return None

        self.tree = self.deleteNodeUtil(self.tree, data)
        return

    def deleteNodeUtil(self, currNode, data):
        node = None
        if currNode == None:
            return currNode

        if currNode.data > data:
            currNode.left = self.deleteNodeUtil(currNode.left, data)
        elif currNode.data < data:
            currNode.right = self.deleteNodeUtil(currNode.right, data)
        else:
            if currNode.left == None:
                return currNode.right
            elif currNode.right == None:
                return currNode.left

            temp = self.__getMinValueNode(currNode.right)
            currNode.data = temp.data
            currNode.freq = temp.freq
            currNode.right = self.deleteNodeUtil(currNode.right, temp.data)

        return currNode

    def getTree(self):
        return self.tree

    def bfsTraversal(self):
        return LinkedListTreeTraversal(self.tree).bfsTraversal()

    def dfsPreOrderTraversal(self):
        return LinkedListTreeTraversal(self.tree).dfsTraversal('pre')

    def dfsInOrderTraversal(self):
        return LinkedListTreeTraversal(self.tree).dfsTraversal('in')

    def dfsPostOrderTraversal(self):
        return LinkedListTreeTraversal(self.tree).dfsTraversal('post')