from ll import PreserveOrderLinkedList


def start():
    ll = PreserveOrderLinkedList()
    while True:
        try:
            print('\n1. INSERT')
            print('2. DELETE HEAD')
            print('3. DELETE MIDDLE')
            print('4. DELETE TAIL')
            print('5. DISPLAY')
            print('6. EXIT')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                data = int(input('Enter the data that you want to insert: '))
                ll.insert(data)
            elif choice == 2:
                data = ll.shift()
                print(f'Data deleted: {data}')
            elif choice == 3:
                num = int(input('Enter the place where you want to delete: '))
                data = ll.deleteMiddle(num)
                print(f'Data deleted: {data}')
            elif choice == 4:
                data = ll.pop()
                print(f'Data deleted: {data}')
            elif choice == 5:
                head, tail = ll.display()
                currNode = head
                if head == None:
                    print('\n-- List is empty --')
                while currNode != None:
                    print(f'Data: {currNode.data}, Pointer: {currNode.next}')
                    currNode = currNode.next
            elif choice == 6:
                break
            else:
                print('Command not recognized!')
        except Exception as error:
            print(error)


if __name__ == "__main__":
    start()
