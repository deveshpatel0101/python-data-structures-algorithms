class UWGraphTraversals:
    def __init__(self, graph):
        self.graph = graph
        self.__queue = []
        self.__stack = []
        self.__visited = []

    def bfsTraversal(self):
        for node in self.graph:
            if node not in self.__visited:
                self.bfsTraversalUtil(node)
        return self.__visited

    def bfsTraversalUtil(self, currNode):
        self.__queue = []
        self.__queue.append(currNode)
        while len(self.__queue) != 0:
            currNode = self.__queue[0]
            self.__queue = self.__queue[1:]

            if currNode in self.__visited:
                continue

            self.__visited.append(currNode)
            for node in self.graph[currNode]:
                if node.name not in self.__visited:
                    self.__queue.append(node.name)

    def dfsTraversal(self):
        for node in self.graph:
            if node not in self.__visited:
                self.dfsTraversalUtil(node)
        return self.__visited

    def dfsTraversalUtil(self, currNode):
        self.__stack = []
        self.__stack.append(currNode)

        while len(self.__stack) != 0:
            currNode = self.__stack.pop()

            if currNode in self.__visited:
                continue

            self.__visited.append(currNode)
            for node in self.graph[currNode]:
                if node.name not in self.__visited and node.name not in self.__stack:
                    self.__stack.append(node.name)
