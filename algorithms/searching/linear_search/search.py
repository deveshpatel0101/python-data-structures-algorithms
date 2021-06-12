class LinearSearch:
    def search(arr, key):
        for index, item in enumerate(arr):
            if item == key:
                return True, index, item
        return False, -1, None
