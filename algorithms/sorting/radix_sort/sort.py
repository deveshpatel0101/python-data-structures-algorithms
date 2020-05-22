class RadixSort:
    def __getNumOfMaxDigits(self, arr):
        max_digits = 0
        for num in arr:
            max_digits = max(max_digits, len(str(num)))
        return max_digits

    def sort(self, arr):
        buckets = [[] for _ in range(10)]
        for index in range(self.__getNumOfMaxDigits(arr)):
            for num in arr:
                num = str(num)
                digit = 0 if index >= len(num) else int(num[::-1][index])
                buckets[digit].append(int(num))

            arr = []
            for bucket in buckets:
                arr.extend(bucket)

            buckets = [[] for _ in range(10)]
        return arr
