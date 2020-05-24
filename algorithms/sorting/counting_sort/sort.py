class CountingSort:
    def sort(self, arr):
        if not arr:
            return arr

        max_val = max(arr)
        sorted_arr = [0 for _ in arr]
        count = [0 for _ in range(max_val+1)]

        for i in arr:
            count[i] += 1

        for i in range(1, max_val+1):
            count[i] += count[i-1]

        for i in range(len(arr)-1, -1, -1):
            sorted_arr[count[arr[i]]-1] = arr[i]
            count[arr[i]] -= 1

        return sorted_arr
