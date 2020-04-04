class LinkedListTreeTraversal:
    def __init__(self, data):
        self.tree = data

    # bfsTraversal is a recursive version of bfs traversal
    def bfsTraversal(self):
        root = self.tree
        queue = []
        path = []

        if self.tree == None:
            return []

        queue.append(root)
        path = self.bfsTraversalUtil(queue, path)
        return path

    # bfsTraversalUtil recursively calls itself to find a bfs traversal path
    def bfsTraversalUtil(self, queue, path):
        if len(queue) == 0:
            return []

        currNode = queue[0]
        path.append(currNode)
        queue = queue[1:]
        childrenIndices = (currNode.left, currNode.right)
        queue.extend(
            [childNode for childNode in childrenIndices if childNode])

        self.bfsTraversalUtil(queue, path)

        return path

    # dfsTraversal calls appropriate recursive pre, in or post order traversal's util function
    def dfsTraversal(self, order):
        root = self.tree
        stack = []
        path = []
        if self.tree == None:
            return []

        stack.append(root)

        if order == 'pre':
            path = self.traversePre(path, self.tree)
        elif order == 'in':
            path = self.traverseIn(path, self.tree)
        elif order == 'post':
            path = self.traversePost(path, self.tree)

        return path

    # parent left right
    # TraversePre is a recursive version of dfs pre-order traversal
    def traversePre(self, path, node):
        if node:
            path.append(node)
            path = self.traversePre(path, node.left)
            path = self.traversePre(path, node.right)

        return path

    # left parent right
    # TraverseIn is a recursive version of dfs in-order traversal
    def traverseIn(self, path, node):
        if node:
            path = self.traverseIn(path, node.left)
            path.append(node)
            path = self.traverseIn(path, node.right)

        return path

    # left right parent
    # TraversePost is a recursive version of dfs post-order traversal
    def traversePost(self, path, node):
        if node:
            path = self.traversePost(path, node.left)
            path = self.traversePost(path, node.right)
            path.append(node)

        return path

    # iteratvieBfsTraversal is an itervative version of bfs traversal
    def iterativeBfsTraversal(self):
        root = self.tree
        queue = []
        path = []
        if self.tree == None:
            return []

        queue.append(root)
        while len(queue) != 0:
            currNode = queue[0]
            path.append(currNode)
            queue = queue[1:]
            childrenIndices = (currNode.left, currNode.right)
            queue.extend(
                [childNode for childNode in childrenIndices if childNode])

        return path

    # parent left right
    # itervativeDfsPreOrderTraversal is iterative version of dfs pre-order traversal
    def iterativeDfsPreOrderTraversal(self):
        stack = []
        root = self.tree
        path = []

        if self.tree == None:
            return []

        stack.append(root)
        while len(stack) != 0:
            currNode = stack[len(stack)-1]
            path.append(currNode)
            stack = stack[:len(stack)-1]
            childrenIndices = (currNode.right, currNode.left)

            stack.extend(
                [childNode for childNode in childrenIndices if childNode])

        return path

    # left parent right
    # iterativeDfsInOrderTraversal is iterative version of dfs in-order traversal
    def iterativeDfsInOrderTraversal(self):
        stack = []
        path = []
        currNode = self.tree
        while True:
            while currNode != None:
                stack.append(currNode)
                currNode = currNode.left

            if currNode == None and len(stack) != 0:
                node = stack[len(stack)-1]
                stack = stack[:len(stack)-1]

                path.append(node)
                currNode = node.right
            if currNode == None and len(stack) == 0:
                break

        return path

    # left right parent
    # iterativeDfsPostOrderTraversal is iterative version of dfs post-order traversal
    def iterativeDfsPostOrderTraversal(self):
        stack = []
        path = []
        currNode = self.tree

        while True:
            while currNode != None:
                (leftChildNode, rightChildNode) = (
                    currNode.left, currNode.right)
                if rightChildNode:
                    stack.append(rightChildNode)
                stack.append(currNode)
                currNode = leftChildNode

            currNode = stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            (leftChildNode, rightChildNode) = (currNode.left, currNode.right)

            if rightChildNode and len(stack) != 0 and stack[len(stack)-1] == rightChildNode:
                stack = stack[:len(stack)-1]
                stack.append(currNode)
                currNode = rightChildNode
            else:
                path.append(currNode)
                currNode = None

            if len(stack) == 0:
                break

        return path


# References:
# Algorithms for iterative in-order traversal: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
# Algorithm for iterative post-order traversal: https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
