class SelectionSort:
    def sort(self, arr):
        for i in range(len(arr)):
            swapInd = i
            for j in range(i, len(arr)):
                if arr[j] < arr[swapInd]:
                    swapInd = j
            arr[i], arr[swapInd] = arr[swapInd], arr[i]
        return arr
