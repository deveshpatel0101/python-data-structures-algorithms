from traversal import LinkedListTreeTraversal


class Node:
    def __init__(self, data):
        self.data = data
        self.freq = 1
        self.left = None
        self.right = None


class SimpleBinaryTree:
    def __init__(self):
        self.tree = None

    def __getLeafNode(self, node):
        while node.left != None or node.right != None:
            if node.left:
                node = node.left
            else:
                node = node.right
        return node

    def insert(self, data):
        root = self.tree
        queue = []
        if self.tree == None:
            self.tree = Node(data)
            return

        queue.append(root)
        while len(queue) != 0:
            currNode = queue[0]
            queue = queue[1:]
            if currNode.data == data:
                currNode.freq += 1
                return
            elif currNode.left == None:
                currNode.left = Node(data)
                return
            elif currNode.right == None:
                currNode.right = Node(data)
                return
            else:
                childrenIndices = (currNode.left, currNode.right)
                queue.extend(
                    [childNode for childNode in childrenIndices if childNode])

    def search(self, data):
        root = self.tree
        queue = []
        if self.tree == None:
            raise Exception('\n-- Data not found --')

        found = {'parent': None, 'sibling': None,
                 'leftChild': None, 'rightChild': None, 'freq': None}

        if self.tree.data == data:
            found['freq'] = self.tree.freq
            found['leftChild'] = self.tree.left.data if self.tree.left else None
            found['rightChild'] = self.tree.right.data if self.tree.right else None
            return found

        queue.append(root)
        while len(queue) != 0:
            currNode = queue[0]
            queue = queue[1:]
            if currNode.left and currNode.left.data == data:
                found['freq'] = currNode.left.freq
                found['parent'] = currNode.data
                found['sibling'] = currNode.right.data if currNode.right else None
                found['leftChild'] = currNode.left.left.data if currNode.left.left else None
                found['rightChild'] = currNode.left.right.data if currNode.left.right else None
                return found
            elif currNode.right and currNode.right.data == data:
                found['freq'] = currNode.right.freq
                found['parent'] = currNode.data
                found['sibling'] = currNode.left.data if currNode.left else None
                found['leftChild'] = currNode.right.left.data if currNode.right.left else None
                found['rightChild'] = currNode.right.right.data if currNode.right.right else None
                return found
            else:
                childrenIndices = (currNode.left, currNode.right)
                queue.extend(
                    [childNode for childNode in childrenIndices if childNode])

    def delete(self, data):
        if self.tree == None:
            return None

        self.tree = self.deleteNodeUtil(self.tree, data)
        return

    def deleteNodeUtil(self, currNode, data):
        node = None
        if currNode == None:
            return currNode

        if currNode.data != data:
            currNode.left = self.deleteNodeUtil(currNode.left, data)
            currNode.right = self.deleteNodeUtil(currNode.right, data)
        else:
            if currNode.freq > 1:
                currNode.freq -= 1
                return currNode
            elif currNode.left == None:
                return currNode.right
            elif currNode.right == None:
                return currNode.left

            temp = self.__getLeafNode(currNode.right)
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
