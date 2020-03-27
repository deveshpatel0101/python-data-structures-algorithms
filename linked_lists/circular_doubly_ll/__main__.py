from ll import CircularDoublyLinkedList


def start():
    ll = CircularDoublyLinkedList()
    while True:
        try:
            print('\n1. INSERT HEAD')
            print('2. INSERT MIDDLE')
            print('3. INSERT TAIL')
            print('4. DELETE HEAD')
            print('5. DELETE MIDDLE')
            print('6. DELETE TAIL')
            print('7. REVERSE')
            print('8. DISPLAY')
            print('9. EXIT')
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
                ll.reverse()
                head, tail = ll.display()
                currNode = head
                if head == None:
                    print('\n-- List is empty --')
                    continue
                while currNode.next != head:
                    print(f'Data: {currNode.data}, Prev: {currNode.prev}, Next: {currNode.next}')
                    currNode = currNode.next
                else:
                    print(f'Data: {currNode.data}, Prev: {currNode.prev}, Next: {currNode.next}')
            elif choice == 8:
                head, tail = ll.display()
                currNode = head
                if head == None:
                    print('\n-- List is empty --')
                    continue
                while currNode.next != head:
                    print(f'Data: {currNode.data}, Prev: {currNode.prev}, Next: {currNode.next}')
                    currNode = currNode.next
                else:
                    print(f'Data: {currNode.data}, Prev: {currNode.prev}, Next: {currNode.next}')
            elif choice == 9:
                break
            else:
                print('Command not recognized!')
        except Exception as error:
            print(error)


if __name__ == "__main__":
    start()
