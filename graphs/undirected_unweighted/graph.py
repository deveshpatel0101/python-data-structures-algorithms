from traversal import UUGraphTraversals


class UUGraph:
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
        self.graph[toNode].append(fromNode)

    def removeNode(self, name):
        # check if the node exists
        if name not in self.graph:
            return

        # delete the node with all edges pointing towards it
        connectedWith = self.graph[name]
        del self.graph[name]
        for node in connectedWith:
            self.graph[node].remove(name)

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
        self.graph[toNode].remove(fromNode)

    def simpleDisplay(self):
        for node, value in self.graph.items():
            print(node, value)

    def bfsTraversal(self):
        return UUGraphTraversals(self.graph).bfsTraversal()

    def dfsTraversal(self):
        return UUGraphTraversals(self.graph).dfsTraversal()
