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
        self.tree = self.insertNodeUtil(self.tree, data)

    def insertNodeUtil(self, currNode, data):
        if currNode == None:
            return Node(data)
        elif data < currNode.data:
            currNode.left = self.insertNodeUtil(currNode.left, data)
        elif data > currNode.data:
            currNode.right = self.insertNodeUtil(currNode.right, data)
        elif currNode.data == data:
            currNode.freq += 1

        return currNode

    def search(self, data):
        return self.searchNodeUtil(self.tree, data)

    def searchNodeUtil(self, currNode, data):
        if currNode == None:
            return None
        elif currNode.data == data:
            return currNode
        elif data < currNode.data:
            return self.searchNodeUtil(currNode.left, data)
        elif data > currNode.data:
            return self.searchNodeUtil(currNode.right, data)

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
            if currNode.freq > 1:
                currNode.freq -= 1
                return currNode
            elif currNode.left == None:
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
