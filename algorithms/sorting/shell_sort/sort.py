class ShellSort:
    def sort(self, arr):
        size = len(arr)
        gap = int(size/2)

        while gap > 0:
            for index in range(size-((size-1) % gap)):
                if arr[index] > arr[gap+index]:
                    arr[index], arr[gap+index] = arr[gap+index], arr[index]

                    j = index
                    while True:
                        if j - gap >= 0 and arr[j-gap] > arr[j]:
                            arr[j-gap], arr[j] = arr[j], arr[j-gap]
                            j -= 1
                        else:
                            break
                if index == (size-1)-gap:
                    break

            gap = int(gap/2)
        return arr
