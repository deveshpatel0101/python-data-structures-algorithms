class BucketSort:
    def __insertionSort(self, arr):
        for marker in range(len(arr)-1):
            element = arr[marker+1]
            index = marker
            while index >= 0 and element < arr[index]:
                arr[index+1] = arr[index]
                index -= 1
            arr[index+1] = element
        return arr

    def sort(self, arr):
        size = len(arr)
        buckets = [[] for _ in range(size)]

        for element in arr:
            buckets[int(size*element)].append(element)

        for index in range(size):
            if buckets[index]:
                buckets[index] = self.__insertionSort(buckets[index])

        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        return arr
