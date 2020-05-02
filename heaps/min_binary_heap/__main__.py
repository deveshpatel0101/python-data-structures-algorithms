from heap import MinHeap


def start():
    heap = MinHeap()
    while True:
        try:
            print('\n1. INSERT')
            print('2. EXTRACT MIN')
            print('3. DELETE')
            print('4. SIMPLE DISPLAY')
            print('5. EXIT')
            choice = int(input('\nEnter your choice: '))

            if choice == 1:
                node = input('Enter the name of the node: ')
                value = int(input('Enter the value of the node: '))
                heap.insert(node, value)
            elif choice == 2:
                node = heap.extractMin()
                if not node:
                    print('\n-- Heap is empty. --')
                else:
                    print(f'Node: {node.name}, Value: {node.value}')
            elif choice == 3:
                node = input('Enter the name of the node: ')
                node = heap.delete(node)
                if not node:
                    print('\n-- Node not found. --')
                else:
                    print(f'Node: {node.name}, Value: {node.value}')
            elif choice == 4:
                heap_arr = heap.getHeap()
                for node in heap_arr:
                    print(f'Node: {node.name}, Value: {node.value}')
            elif choice == 5:
                break
            else:
                print('Command not recognized.')
        except Exception as error:
            print(error)


if __name__ == '__main__':
    start()

# heap.insert('a', 5)
# heap.insert('b', 8)
# heap.insert('c', 1)
# heap.insert('d', 4)
# heap.insert('e', 3)
# heap.insert('f', 7)
# heap.insert('g', 2)
# heap.insert('h', 9)
# heap.insert('i', 6)
