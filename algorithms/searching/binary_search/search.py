class BinarySearch:
    def search(self, arr, key):
        if len(arr) == 0:
            return False, None
        left, right = 0, len(arr)-1

        while left <= right:
            middle = (right + left) // 2

            if arr[middle] == key:
                return True, middle
            elif arr[middle] > key:
                right = middle-1
            elif arr[middle] < key:
                left = middle+1

        return False, None
