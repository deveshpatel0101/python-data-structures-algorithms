from sort import SelectionSort


def start():
    selection_sort = SelectionSort()
    try:
        size = int(input('Enter the number of elements: '))
        arr = []
        print('Start entering elements:')
        for i in range(size):
            arr.append(int(input()))
        print('Sorted Array is:')
        print(selection_sort.sort(arr))
    except Exception as error:
        print(error)


if __name__ == '__main__':
    start()
