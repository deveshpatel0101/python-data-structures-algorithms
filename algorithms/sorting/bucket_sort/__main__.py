from sort import BucketSort


def start():
    bucket_sort = BucketSort()
    try:
        size = int(input('Enter the number of elements: '))
        arr = []
        print('Start entering elements:')
        for i in range(size):
            arr.append(float(input()))
        print('Sorted Array is:')
        print(bucket_sort.sort(arr))
    except Exception as error:
        print(error)


if __name__ == '__main__':
    start()
