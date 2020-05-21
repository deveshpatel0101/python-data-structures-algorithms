class QuickSort:
    def sort(self, arr):
        self.sortUtil(arr, 0, len(arr)-1)
        return arr

    def sortUtil(self, arr, low, high):
        if low >= high:
            return
        idx = self.findPivot(arr, 0, high)
        self.sortUtil(arr, low, idx-1)
        self.sortUtil(arr, idx+1, high)

    def findPivot(self, arr, low, high):
        pivot = high
        i = -1
        j = 0

        while j < pivot:
            if arr[pivot] > arr[j]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

            j += 1
        for idx in range(pivot, i+1, -1):
            arr[idx], arr[idx-1] = arr[idx-1], arr[idx]

        return i+1
