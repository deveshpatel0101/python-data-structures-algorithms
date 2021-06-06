class HeapSort:
    def __init__(self):
        self.__heap = []
        self.__size = 0

    def sort(self, arr):
        size = len(arr)
        self.__heap = arr
        self.__size = size

        for index in range(size-1, -1, -1):
            self.bubbleUp(index)

        for index in range(size):
            self.extractMax()

        return self.__heap

    def __getParent(self, index):
        return 0 if index == 0 else int((index-1)/2)

    # getMaxValueChild will return an index of child node from parentIndex having the max value
    def __getMaxValueChild(self, parentIndex):
        leftChildIndex = parentIndex*2+1
        rightChildIndex = parentIndex*2+2
        if leftChildIndex >= self.__size:
            leftChildIndex = None
        if rightChildIndex >= self.__size:
            rightChildIndex = None

        if leftChildIndex is None:
            return rightChildIndex
        elif rightChildIndex is None:
            return leftChildIndex
        elif self.__heap[leftChildIndex] > self.__heap[rightChildIndex]:
            return leftChildIndex

        return rightChildIndex

    # bubbleUp will traverse the heap in upward direction while shifting the nodes in proper places
    def bubbleUp(self, index=-1):
        index = index if index != -1 else self.__size-1
        while index != 0:
            parentIndex = self.__getParent(index)
            if self.__heap[parentIndex] >= self.__heap[index]:
                break
            self.__heap[parentIndex], self.__heap[index] = self.__heap[index], self.__heap[parentIndex]
            index = parentIndex

    # extractMax will remove a node from the heap whose value is maximum
    def extractMax(self):
        if self.__size == 0:
            return None

        node = self.__heap[0]

        # swap the first element with the last element
        self.__heap[0], self.__heap[self.__size -
                                    1] = self.__heap[self.__size-1], self.__heap[0]
        self.__size -= 1

        # bubbledown the heap
        if self.__size > 0:
            self.bubbleDown()
        return node

    # bubbleDown will traverse the heap in downward direction while shifting the nodes in proper places
    def bubbleDown(self):
        index = 0
        while index < self.__size:
            nextIndex = self.__getMaxValueChild(index)
            if not nextIndex:
                return

            if not (self.__heap[index] < self.__heap[nextIndex]):
                break

            self.__heap[index], self.__heap[nextIndex] = self.__heap[nextIndex], self.__heap[index]
            index = nextIndex
