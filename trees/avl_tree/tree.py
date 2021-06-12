from trees.avl_tree.traversal import LLTreeTraversal


class Node:
    def __init__(self, value):
        self.value = value
        self.freq = 1
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.__root = None

    def insert(self, value):
        self.__root = self.__insertUtil(self.__root, value)

    def __insertUtil(self, node, value):
        if node == None:
            node = Node(value)
            return node

        if value > node.value:
            node.right = self.__insertUtil(node.right, value)
        elif value < node.value:
            node.left = self.__insertUtil(node.left, value)
        else:
            node.freq += 1

        node.height = max(self.__getHeight(node.left),
                          self.__getHeight(node.right)) + 1

        bf = self.__getBalancingFactor(node)

        # LL case
        if bf > 1 and value < node.left.value:
            return self.__rightRotate(node)

        # RR case
        if bf < -1 and value > node.right.value:
            return self.__leftRotate(node)

        # LR case
        if bf > 1 and value > node.left.value:
            node.left = self.__leftRotate(node.left)
            return self.__rightRotate(node)

        # RL case
        if bf < -1 and value < node.right.value:
            node.right = self.__rightRotate(node.right)
            return self.__leftRotate(node)

        return node

    def __getBalancingFactor(self, node):
        if node == None:
            return 0
        return self.__getHeight(node.left) - self.__getHeight(node.right)

    def __getHeight(self, node):
        return 0 if node is None else node.height

    def remove(self, value):
        self.__root = self.__removeUtil(self.__root, value, True)

    def __removeUtil(self, node, value, useFreq):
        if node is None:
            return None
        elif node.value > value:
            node.left = self.__removeUtil(node.left, value, useFreq)
        elif node.value < value:
            node.right = self.__removeUtil(node.right, value, useFreq)
        else:
            if useFreq and node.freq > 1:
                node.freq -= 1
                return
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.getMinValueNode(node.right)
            node.value = temp.value
            node.freq = temp.freq
            node.right = self.__removeUtil(node.right, node.value, False)

        if node is None:
            return

        node.height = max(self.__getHeight(node.left),
                          self.__getHeight(node.right)) + 1

        bf = self.__getBalancingFactor(node)

        # LL case
        if bf > 1 and self.__getBalancingFactor(node.left) >= 0:
            return self.__rightRotate(node)

        # RR case
        if bf < -1 and self.__getBalancingFactor(node.right) <= 0:
            return self.__leftRotate(node)

        # LR case
        if bf > 1 and self.__getBalancingFactor(node.left) < 0:
            node.left = self.__leftRotate(node.left)
            return self.__rightRotate(node)

        # RL case
        if bf < -1 and self.__getBalancingFactor(node.right) > 0:
            node.right = self.__rightRotate(node.right)
            return self.__leftRotate(node)

        return node

    def __leftRotate(self, node):
        b = node.right
        t = b.left

        b.left = node
        node.right = t
        node.height = max(self.__getHeight(node.left), self.__getHeight(node.right)) + 1
        b.height = max(self.__getHeight(b.left), self.__getHeight(b.right)) + 1
        return b

    def __rightRotate(self, node):
        b = node.left
        t = b.right

        b.right = node
        node.left = t

        node.height = max(self.__getHeight(node.left), self.__getHeight(node.right)) + 1
        b.height = max(self.__getHeight(b.left), self.__getHeight(b.right)) + 1
        return b

    def search(self, value):
        node = self.__searchNodeUtil(self.__root, value)
        if node is None:
            return node

        data = {'value': node.value, 'freq': node.freq}
        if node.left:
            data['left'] = node.left.value
        if node.right:
            data['right'] = node.right.value
        return data

    def __searchNodeUtil(self, node, key):
        if node == None:
            return None
        elif node.value == key:
            return node
        elif key < node.value:
            return self.__searchNodeUtil(node.left, key)
        elif key > node.value:
            return self.__searchNodeUtil(node.right, key)

    def getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    def getBFSTraversal(self):
        return LLTreeTraversal(self.__root).bfsTraversal()

    def getDFSPreOrderTraversal(self):
        return LLTreeTraversal(self.__root).dfsTraversal('pre')

    def getDFSInOrderTraversal(self):
        return LLTreeTraversal(self.__root).dfsTraversal('in')

    def getDFSPostOrderTraversal(self):
        return LLTreeTraversal(self.__root).dfsTraversal('post')
