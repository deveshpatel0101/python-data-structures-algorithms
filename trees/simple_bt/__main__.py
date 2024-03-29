from tree import SimpleBinaryTree


def start():
    tree = SimpleBinaryTree()
    while True:
        try:
            print('\n1. INSERT')
            print('2. DELETE')
            print('3. SEARCH')
            print('4. BFS')
            print('5. DFS PRE-ORDER')
            print('6. DFS IN-ORDER')
            print('7. DFS POST-ORDER')
            print('8. SIMPLE DISPLAY')
            print('9. EXIT')
            choice = int(input('\nEnter your choice: '))

            if choice == 1:
                data = int(
                    input('Enter the element that you want to insert: '))
                tree.insert(data)
            elif choice == 2:
                data = int(
                    input('Enter the element that you want to delete: '))
                tree.delete(data)
            elif choice == 3:
                data = int(
                    input('Enter the element that you want to search: '))
                foundData = tree.search(data)
                if foundData is not None:
                    print(f'Data: {foundData.data}, Freq: {foundData.freq}')
                else:
                    print('\n-- Data not found! --')
            elif choice == 4:
                path = tree.bfsTraversal()
                if len(path) == 0:
                    print('\n-- Tree is empty --')
                for node in path:
                    print(f'Data: {node.data}, Freq: {node.freq}')
            elif choice == 5:
                path = tree.dfsPreOrderTraversal()
                if len(path) == 0:
                    print('\n-- Tree is empty --')
                for node in path:
                    print(f'Data: {node.data}, Freq: {node.freq}')
            elif choice == 6:
                path = tree.dfsInOrderTraversal()
                if len(path) == 0:
                    print('\n-- Tree is empty --')
                for node in path:
                    print(f'Data: {node.data}, Freq: {node.freq}')
            elif choice == 7:
                path = tree.dfsPostOrderTraversal()
                if len(path) == 0:
                    print('\n-- Tree is empty --')
                for node in path:
                    print(f'Data: {node.data}, Freq: {node.freq}')
            elif choice == 8:
                tree.simpleDisplay()
            elif choice == 9:
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
