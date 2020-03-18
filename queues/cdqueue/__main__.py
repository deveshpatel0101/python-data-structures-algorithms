from cdqueue import CircularDoubleEndedQueue


def start():
    queue = CircularDoubleEndedQueue()
    while True:
        try:
            print('\n1. INSERT FRONT')
            print('2. INSERT REAR')
            print('3. DELETE FRONT')
            print('4. DELETE REAR')
            print('5. GET POINTERS')
            print('6. DISPLAY')
            print('7. EXIT')
            choice = int(input('\nEnter your choice: '))

            if choice == 1:
                element = int(
                    input('Enter the element that you want to insert: '))
                queue.insertFront(element)
                (front, rear) = queue.get_pointers()
                print(f'\nValues after insertion FRONT: {front}, REAR: {rear}')
                print(f'{queue.display()}')
            elif choice == 2:
                element = int(
                    input('Enter the element that you want to insert: '))
                queue.insertRear(element)
                (front, rear) = queue.get_pointers()
                print(f'\nValues after insertion FRONT: {front}, REAR: {rear}')
                print(f'{queue.display()}')
            elif choice == 3:
                element = queue.deleteFront()
                print(f'\nElement deleted: {element}')
                (front, rear) = queue.get_pointers()
                print(f'Values after deletion FRONT: {front}, REAR: {rear}')
            elif choice == 4:
                element = queue.deleteRear()
                print(f'\nElement deleted: {element}')
                (front, rear) = queue.get_pointers()
                print(f'Values after deletion FRONT: {front}, REAR: {rear}')
            elif choice == 5:
                (front, rear) = queue.get_pointers()
                print(f'\nPointer values are FRONT: {front}, REAR: {rear}')
            elif choice == 6:
                print(f'{queue.display()}')
            elif choice == 7:
                break
            else:
                print("Command not recognized.")
        except Exception as error:
            print(error)


if __name__ == "__main__":
    start()
