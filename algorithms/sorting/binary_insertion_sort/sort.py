class BinaryInsertionSort:
    def sort(self, arr):
        for idx in range(1, len(arr)):
            val = arr[idx]
            insertIdx = self.binary_search(arr, val, 0, idx-1)
            arr = arr[:insertIdx] + [val] + arr[insertIdx:idx] + arr[idx+1:]
        return arr

    def binary_search(self, arr, val, start, end):
        if start == end:
            if arr[start] > val:
                return start
            else:
                return start+1

        if start > end:
            return start

        mid = (start+end) // 2
        if arr[mid] < val:
            return self.binary_search(arr, val, mid+1, end)
        elif arr[mid] > val:
            return self.binary_search(arr, val, start, mid-1)
        else:
            return mid
