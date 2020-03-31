class ArrayTreeTraversal:
    def __init__(self, data):
        self.tree = data
        self.size = len(data)

    def __getChildrenIndices(self, index):
        leftChildIndex = (index*2)+1
        rightChildIndex = (index*2)+2

        if not (leftChildIndex < len(self.tree) and self.tree[leftChildIndex]):
            leftChildIndex = None
        if not (rightChildIndex < len(self.tree) and self.tree[rightChildIndex]):
            rightChildIndex = None

        return (leftChildIndex, rightChildIndex)

    # bfsTraversal is a recursive version of bfs traversal
    def bfsTraversal(self):
        root = 0
        queue = []
        path = []

        if self.tree[root] == None:
            return []

        queue.append(root)
        path = self.bfsTraversalUtil(queue, path)
        return path

    # bfsTraversalUtil recursively calls itself to find a bfs traversal path
    def bfsTraversalUtil(self, queue, path):
        if len(queue) == 0:
            return []

        currIndex = queue[0]
        path.append(self.tree[currIndex])
        queue = queue[1:]
        childrenIndices = self.__getChildrenIndices(currIndex)
        queue.extend(
            [childIndex for childIndex in childrenIndices if childIndex])

        self.bfsTraversalUtil(queue, path)

        return path

    # iteratvieBfsTraversal is an itervative version of bfs traversal
    def iterativeBfsTraversal(self):
        root = 0
        queue = []
        path = []
        if self.tree[root] == None:
            return []

        queue.append(root)
        while len(queue) != 0:
            currIndex = queue[0]
            path.append(self.tree[currIndex])
            queue = queue[1:]
            childrenIndices = self.__getChildrenIndices(currIndex)
            queue.extend(
                [childIndex for childIndex in childrenIndices if childIndex])

        return path

    # dfsTraversal calls appropriate recursive pre, in or post order traversals
    def dfsTraversal(self, order):
        root = 0
        stack = []
        path = []
        if self.tree[root] == None:
            return []

        stack.append(root)

        if order == 'pre':
            path = self.traversePre(path, 0)
        elif order == 'in':
            path = self.traverseIn(path, 0)
        elif order == 'post':
            path = self.traversePost(path, 0)

        return path

    # parent left right
    # TraversePre is a recursive version of dfs pre-order traversal
    def traversePre(self, path, index):
        if len(self.tree) > index and self.tree[index]:
            path.append(self.tree[index])
            path = self.traversePre(path, (index*2)+1)
            path = self.traversePre(path, (index*2)+2)

        return path

    # left parent right
    # TraverseIn is a recursive version of dfs in-order traversal
    def traverseIn(self, path, index):
        if len(self.tree) > index and self.tree[index]:
            path = self.traverseIn(path, (index*2)+1)
            path.append(self.tree[index])
            path = self.traverseIn(path, (index*2)+2)

        return path

    # left right parent
    # TraversePost is a recursive version of dfs post-order traversal
    def traversePost(self, path, index):
        if len(self.tree) > index and self.tree[index]:
            path = self.traversePost(path, (index*2)+1)
            path = self.traversePost(path, (index*2)+2)
            path.append(self.tree[index])

        return path

    # parent left right
    # itervativeDfsPreOrderTraversal is iterative version of dfs pre-order traversal
    def iterativeDfsPreOrderTraversal(self):
        stack = []
        root = 0
        path = []

        if self.tree[root] == None:
            return []

        stack.append(root)
        while len(stack) != 0:
            parentIndex = stack[len(stack)-1]
            path.append(self.tree[parentIndex])
            stack = stack[:len(stack)-1]
            childrenIndices = self.__getChildrenIndices(parentIndex)
            childrenIndices = childrenIndices[::-1]

            stack.extend(
                [childIndex for childIndex in childrenIndices if childIndex])

        return path

    # left parent right
    # iterativeDfsInOrderTraversal is iterative version of dfs in-order traversal
    def iterativeDfsInOrderTraversal(self):
        stack = []
        path = []
        currIndex = 0
        while True:
            while currIndex != None:
                stack.append(currIndex)
                currIndex = self.__getChildrenIndices(currIndex)[0]

            if currIndex == None and len(stack) != 0:
                item = stack[len(stack)-1]
                stack = stack[:len(stack)-1]

                path.append(self.tree[item])
                currIndex = self.__getChildrenIndices(item)[1]
            if currIndex == None and len(stack) == 0:
                break

        return path

    # left right parent
    # iterativeDfsPostOrderTraversal is iterative version of dfs post-order traversal
    def iterativeDfsPostOrderTraversal(self):
        stack = []
        path = []
        currIndex = 0

        while True:
            while currIndex != None:
                (leftChildIndex, rightChildIndex) = self.__getChildrenIndices(currIndex)
                if rightChildIndex:
                    stack.append(rightChildIndex)
                stack.append(currIndex)
                currIndex = leftChildIndex

            currIndex = stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            (leftChildIndex, rightChildIndex) = self.__getChildrenIndices(currIndex)

            if rightChildIndex and len(stack) != 0 and stack[len(stack)-1] == rightChildIndex:
                stack = stack[:len(stack)-1]
                stack.append(currIndex)
                currIndex = rightChildIndex
            else:
                path.append(self.tree[currIndex])
                currIndex = None

            if len(stack) == 0:
                break

        return path


# References:
# Algorithms for iterative in-order traversal: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
# Algorithm for iterative post-order traversal: https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
