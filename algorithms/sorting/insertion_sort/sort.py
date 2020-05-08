class InsertionSort:
    def sort(self, arr):
        for marker in range(len(arr)-1):
            element = arr[marker+1]
            index = marker
            while index >= 0 and element < arr[index]:
                arr[index+1] = arr[index]
                index -= 1
            arr[index+1] = element
        return arr
