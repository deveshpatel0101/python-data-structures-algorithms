from ll import SinglyLinkedList


def start():
    ll = SinglyLinkedList()
    while True:
        try:
            print('\n1. INSERT HEAD')
            print('2. INSERT MIDDLE')
            print('3. INSERT TAIL')
            print('4. DELETE HEAD')
            print('5. DELETE MIDDLE')
            print('6. DELETE TAIL')
            print('7. DISPLAY')
            print('8. EXIT')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                data = input('Enter the data that you want to insert: ')
                ll.unshift(data)
            elif choice == 2:
                num = int(input('Enter the place where you want to insert: '))
                data = input('Enter the data that you want to insert: ')
                ll.insertMiddle(num, data)
            elif choice == 3:
                data = input('Enter the data that you want to insert: ')
                ll.push(data)
            elif choice == 4:
                data = ll.shift()
                print(f'Data deleted: {data}')
            elif choice == 5:
                num = int(input('Enter the place where you want to delete: '))
                data = ll.deleteMiddle(num)
                print(f'Data deleted: {data}')
            elif choice == 6:
                data = ll.pop()
                print(f'Data deleted: {data}')
            elif choice == 7:
                head, tail = ll.display()
                currNode = head
                if head == None:
                    print('\n-- List is empty --')
                while currNode != None:
                    print(f'Data: {currNode.data}, Pointer: {currNode.next}')
                    currNode = currNode.next
            elif choice == 8:
                break
            else:
                print('Command not recognized!')
        except Exception as error:
            print(error)


if __name__ == "__main__":
    start()
