class LinearSearch:
    def search(self, arr, key):
        for index, item in enumerate(arr):
            if item == key:
                return True, index, item
        return False, None
