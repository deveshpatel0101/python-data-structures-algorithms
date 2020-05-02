class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class MinHeap:
    def __init__(self):
        self.min_heap = []

    def __getParent(self, index):
        if index == 0:
            return 0

        if index % 2 != 0:
            return int((index-1)/2)
        return int((index-2)/2)

    # getMinValueChild will return an index of child node of parentIndex having the least value
    def __getMinValueChild(self, parentIndex):
        leftChildIndex = parentIndex*2+1
        rightChildIndex = parentIndex*2+2
        if leftChildIndex >= len(self.min_heap):
            leftChildIndex = None
        if rightChildIndex >= len(self.min_heap):
            rightChildIndex = None

        if not leftChildIndex and not rightChildIndex:
            return None
        elif leftChildIndex and rightChildIndex and self.min_heap[leftChildIndex].value < self.min_heap[rightChildIndex].value:
            return leftChildIndex
        elif leftChildIndex and rightChildIndex and self.min_heap[leftChildIndex].value > self.min_heap[rightChildIndex].value:
            return rightChildIndex
        return leftChildIndex if leftChildIndex else rightChildIndex

    def getHeap(self):
        return self.min_heap

    # insert will insert a node in the heap
    def insert(self, name, value):
        self.min_heap.append(Node(name, value))
        self.minHeapify()

    # minHeapify will traverse the heap in upward direction while shifting the nodes in proper places
    def minHeapify(self, index=-1):
        index = index if index != -1 else len(self.min_heap)-1
        while index != 0:
            parentIndex = self.__getParent(index)
            if self.min_heap[parentIndex].value <= self.min_heap[index].value:
                break
            self.min_heap[parentIndex], self.min_heap[index] = self.min_heap[index], self.min_heap[parentIndex]
            index = parentIndex

    # extractMin will remove a node from the heap whose value will the least in the heap
    def extractMin(self):
        if len(self.min_heap) == 0:
            return None

        node = self.min_heap[0]

        # remove the first element
        self.min_heap[0] = self.min_heap[-1]
        # replace the first element with the last element
        self.min_heap = self.min_heap[:-1]
        # bubbledown the heap
        if len(self.min_heap) > 0:
            self.bubbleDown()

        return node

    # bubbleDown will traverse the heap in downward direction while shifting the nodes in proper places
    def bubbleDown(self):
        index = 0
        while index < len(self.min_heap):
            nextIndex = self.__getMinValueChild(index)
            if not nextIndex:
                return

            if not self.min_heap[index].value > self.min_heap[nextIndex].value:
                break

            self.min_heap[index], self.min_heap[nextIndex] = self.min_heap[nextIndex], self.min_heap[index]
            index = nextIndex

    def delete(self, name):
        node = None
        for index in range(len(self.min_heap)):
            if self.min_heap[index].name == name:
                node = Node(name, self.min_heap[index].value)
                self.min_heap[index].value = float('-inf')
                self.minHeapify(index)
        if node:
            self.extractMin()
        return node
