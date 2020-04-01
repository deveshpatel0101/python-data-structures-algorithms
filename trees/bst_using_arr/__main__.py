from tree import BinarySearchTree


def start():
    tree = BinarySearchTree()
    while True:
        try:
            print('\n1. INSERT')
            print('2. SEARCH')
            print('3. BFS')
            print('4. DFS PRE-ORDER')
            print('5. DFS IN-ORDER')
            print('6. DFS POST-ORDER')
            print('7. SIMPLE DISPLAY')
            print('8. EXIT')
            choice = int(input('\nEnter your choice: '))

            if choice == 1:
                element = int(
                    input('Enter the element that you want to insert: '))
                tree.insert(element)
            elif choice == 2:
                data = int(
                    input('Enter the element that you want to search: '))
                foundData = tree.search(data)
                print(f'Data: {foundData["found"]}, Freq: {foundData["freq"]}')
                print(
                    f'Parent: {foundData["parent"]}, Sibling: {foundData["sibling"]}')
                print(
                    f'Left Child: {foundData["leftChild"]}, Right Child: {foundData["rightChild"]}')
            elif choice == 3:
                path = tree.bfsTraversal()
                if len(path) == 0:
                    print('\n-- Tree is empty --')
                for node in path:
                    print(f'Data: {node.data}, Freq: {node.freq}')
            elif choice == 4:
                path = tree.dfsPreOrderTraversal()
                if len(path) == 0:
                    print('\n-- Tree is empty --')
                for node in path:
                    print(f'Data: {node.data}, Freq: {node.freq}')
            elif choice == 5:
                path = tree.dfsInOrderTraversal()
                if len(path) == 0:
                    print('\n-- Tree is empty --')
                for node in path:
                    print(f'Data: {node.data}, Freq: {node.freq}')
            elif choice == 6:
                path = tree.dfsPostOrderTraversal()
                if len(path) == 0:
                    print('\n-- Tree is empty --')
                for node in path:
                    print(f'Data: {node.data}, Freq: {node.freq}')
            elif choice == 7:
                tree.simpleDisplay()
            elif choice == 8:
                break
            else:
                print('Command not recognized.')
        except Exception as error:
            print(error)


if __name__ == '__main__':
    start()

# tree.insert(1)
# tree.insert(-10)
# tree.insert(20)
# tree.insert(-15)
# tree.insert(-5)
# tree.insert(15)
# tree.insert(25)
# tree.insert(-18)
# tree.insert(-11)
# tree.insert(-7)
# tree.insert(-2)
# tree.insert(14)
# tree.insert(17)
# tree.insert(24)
# tree.insert(28)
# tree.insert(-5)
# tree.insert(25)
