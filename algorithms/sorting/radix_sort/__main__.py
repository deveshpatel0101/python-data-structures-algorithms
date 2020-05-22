from sort import RadixSort


def start():
    radix_sort = RadixSort()
    try:
        size = int(input('Enter the number of elements: '))
        arr = []
        print('Start entering elements:')
        for i in range(size):
            temp = int(input())
            if temp < 0:
                print('\n-- Current implementation only works with positive integers. --')
                return
            arr.append(temp)
        print('Sorted Array is:')
        print(radix_sort.sort(arr))
    except Exception as error:
        print(error)


if __name__ == '__main__':
    start()
