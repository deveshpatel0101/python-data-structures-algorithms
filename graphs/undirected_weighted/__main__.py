from graph import UWGraph


def start():
    graph = UWGraph()
    while True:
        try:
            print('\n1. ADD A NODE')
            print('2. ADD AN EDGE')
            print('3. REMOVE A NODE')
            print('4. REMOVE AN EDGE')
            print('5. SIMPLE DISPLAY')
            print('6. DISPLAY USING BFS')
            print('7. DISPLAY USING DFS')
            print('8. EXIT')
            choice = int(input('\nEnter your choice: '))

            if choice == 1:
                name = input('Enter the name of the node: ')
                graph.addNode(name)
            elif choice == 2:
                fromNode = input('Enter the starting node: ')
                toNode = input('Enter the destination node: ')
                graph.addEdge(fromNode, toNode)
            elif choice == 3:
                name = input('Enter the name of the node: ')
                graph.removeNode(name)
            elif choice == 4:
                fromNode = input('Enter the starting node: ')
                toNode = input('Enter the destination node: ')
                graph.removeEdge(fromNode, toNode)
            elif choice == 5:
                print(
                    'n: represents name of the node, w: represents weight of that edge')
                graph.simpleDisplay()
            elif choice == 6:
                path = graph.bfsTraversal()
                if len(path) == 0:
                    print('\n-- graph is empty --')
                else:
                    print(path)
            elif choice == 7:
                path = graph.dfsTraversal()
                if len(path) == 0:
                    print('\n-- graph is empty --')
                else:
                    print(path)
            elif choice == 8:
                break
            else:
                print('Command not recognized.')
        except Exception as error:
            print(error)


if __name__ == '__main__':
    start()

# graph.addNode('0')
# graph.addNode('1')
# graph.addNode('2')
# graph.addNode('3')
# graph.addNode('4')
# graph.addNode('5')
# graph.addEdge('0', '1', 5)
# graph.addEdge('0', '2', 7)
# graph.addEdge('1', '3', 3)
# graph.addEdge('1', '4', 8)
# graph.addEdge('2', '4', 2)
# graph.addEdge('3', '4', 1)
# graph.addEdge('3', '5', 7)
# graph.addEdge('4', '5', 9)
# bfs: 012345
# dfs: 024531

# graph.addNode('a')
# graph.addNode('b')
# graph.addNode('c')
# graph.addNode('d')
# graph.addNode('e')
# graph.addNode('f')
# graph.addEdge('a', 'b', 5)
# graph.addEdge('a', 'c', 8)
# graph.addEdge('b', 'd', 1)
# graph.addEdge('c', 'e', 4)
# bfs: abcdef
# dfs: acebdf
