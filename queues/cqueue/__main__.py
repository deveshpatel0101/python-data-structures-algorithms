from cqueue import CircularQueue


def start():
    queue = CircularQueue()
    while True:
        try:
            print('\n1. INSERT')
            print('2. DELETE')
            print('3. GET POINTERS')
            print('4. DISPLAY')
            print('5. EXIT')
            choice = int(input('\nEnter your choice: '))

            if choice == 1:
                element = int(
                    input('Enter the element that you want to insert: '))
                queue.insert(element)
                (front, rear) = queue.get_pointers()
                print(f'\nValues after insertion FRONT: {front}, REAR: {rear}')
                print(f'{queue.display()}')

            elif choice == 2:
                element = queue.delete()
                print(f'\nElement deleted: {element}')
                (front, rear) = queue.get_pointers()
                print(f'Values after deletion FRONT: {front}, REAR: {rear}')
            elif choice == 3:
                (front, rear) = queue.get_pointers()
                print(f'\nPointer values are FRONT: {front}, REAR: {rear}')
            elif choice == 4:
                print(f'{queue.display()}')
            elif choice == 5:
                break
            else:
                print("Command not recognized.")
        except Exception as error:
            print(error)


if __name__ == "__main__":
    start()
