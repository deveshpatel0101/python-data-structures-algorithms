from sort import QuickSort


def start():
    quick_sort = QuickSort()
    try:
        size = int(input('Enter the number of elements: '))
        arr = []
        print('Start entering elements:')
        for i in range(size):
            arr.append(int(input()))
        print('Sorted Array is:')
        print(quick_sort.sort(arr))
    except Exception as error:
        print(error)


if __name__ == '__main__':
    start()
