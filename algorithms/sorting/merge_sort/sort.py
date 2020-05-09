class MergeSort:
    def sort(self, arr):
        self.split(arr)
        return arr

    def split(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            self.split(left)
            self.split(right)
            self.combine(left, right, arr)

    def combine(self, left, right, arr):
        leftIndex = rightIndex = index = 0

        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                arr[index] = left[leftIndex]
                leftIndex += 1
                index += 1
            else:
                arr[index] = right[rightIndex]
                rightIndex += 1
                index += 1

        while leftIndex < len(left):
            arr[index] = left[leftIndex]
            leftIndex += 1
            index += 1

        while rightIndex < len(right):
            arr[index] = right[rightIndex]
            rightIndex += 1
            index += 1
