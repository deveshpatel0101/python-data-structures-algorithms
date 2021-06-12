class InterpolationSearch:
    def search(self, arr, key):
        low, high = 0, len(arr)-1

        while arr[low] <= key and arr[high] >= key:
            pos = low + \
                int(((key - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            if arr[pos] == key:
                return True, pos
            elif key < arr[pos]:
                high = pos-1
            elif key > arr[pos]:
                low = pos+1

        return False, None
