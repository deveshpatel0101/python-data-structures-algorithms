from traversal import DUGraphTraversals


class DUGraph:
    def __init__(self):
        self.graph = {}

    def addNode(self, name):
        # check if the node exists
        if name in self.graph:
            return

        # create the node
        self.graph[name] = []

    def addEdge(self, fromNode, toNode):
        # check if both the nodes exist otherwise create one
        if fromNode not in self.graph:
            self.addNode(fromNode)
        if toNode not in self.graph:
            self.addNode(toNode)

        # check if an edge exists
        for node in self.graph[fromNode]:
            if node == toNode:
                return

        # create an edge
        self.graph[fromNode].append(toNode)

    def removeNode(self, name):
        # check if the node exists
        if name not in self.graph:
            return

        # delete the node with all edges pointing towards it
        for node in self.graph.keys():
            if name in self.graph[node]:
                self.graph[node].remove(name)
        del self.graph[name]

    def removeEdge(self, fromNode, toNode):
        # check if both nodes exist
        if fromNode not in self.graph:
            return
        if toNode not in self.graph:
            return

        # check if an edge exists
        if toNode not in self.graph[fromNode]:
            return

        # remove an edge
        self.graph[fromNode].remove(toNode)

    def simpleDisplay(self):
        for node, value in self.graph.items():
            print(node, value)

    def bfsTraversal(self):
        return DUGraphTraversals(self.graph).bfsTraversal()

    def dfsTraversal(self):
        return DUGraphTraversals(self.graph).dfsTraversal()
