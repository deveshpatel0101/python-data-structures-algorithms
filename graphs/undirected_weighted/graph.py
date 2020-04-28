from traversal import UWGraphTraversals


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class UWGraph:
    def __init__(self):
        self.graph = {}

    def addNode(self, name):
        # check if the node exists
        if name in self.graph:
            return

        # create the node
        self.graph[name] = []

    def addEdge(self, fromNode, toNode, weight):
        # check if both the nodes exist otherwise create one
        if fromNode not in self.graph:
            self.addNode(fromNode)
        if toNode not in self.graph:
            self.addNode(toNode)

        # check if an edge exists
        for node in self.graph[fromNode]:
            if node.name == toNode:
                return

        # create an edge
        self.graph[fromNode].append(Node(toNode, weight))
        self.graph[toNode].append(Node(fromNode, weight))

    def removeNode(self, name):
        # check if the node exists
        if name not in self.graph:
            return

        # delete the node with all edges pointing towards it
        for node in self.graph[name]:
            self.graph[node.name] = list(
                filter(lambda item: item.name != name, self.graph[node.name]))
        del self.graph[name]

    def removeEdge(self, fromNode, toNode):
        # check if both nodes exist
        if fromNode not in self.graph:
            return
        if toNode not in self.graph:
            return

        # check if an edge exists
        isEdge = [node for node in self.graph[fromNode] if node.name == toNode]
        if not isEdge:
            return

        # remove an edge
        self.graph[fromNode] = list(filter(
            lambda node: node.name != toNode, self.graph[fromNode]))
        self.graph[toNode] = list(filter(
            lambda node: node.name != fromNode, self.graph[toNode]))

    def simpleDisplay(self):
        for key, value in self.graph.items():
            print(key, [{'n': node.name, 'w': node.weight} for node in value])

    def bfsTraversal(self):
        return UWGraphTraversals(self.graph).bfsTraversal()

    def dfsTraversal(self):
        return UWGraphTraversals(self.graph).dfsTraversal()
