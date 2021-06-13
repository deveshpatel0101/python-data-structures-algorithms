class Node:
    def __init__(self, name, priority):
        self.priority = priority
        self.name = name


class MaxHeap:
    def __init__(self):
        self.max_heap = []

    def __getParent(self, index):
        if index == 0:
            return 0

        if index % 2 != 0:
            return int((index-1)/2)
        return int((index-2)/2)

    # getMaxValueChild will return an index of child node of parentIndex having the least value
    def __getMaxValueChild(self, parentIndex):
        leftChildIndex = parentIndex*2+1
        rightChildIndex = parentIndex*2+2
        if leftChildIndex >= len(self.max_heap):
            leftChildIndex = None
        if rightChildIndex >= len(self.max_heap):
            rightChildIndex = None

        if not leftChildIndex and not rightChildIndex:
            return None
        elif leftChildIndex and rightChildIndex and self.max_heap[leftChildIndex].priority > self.max_heap[rightChildIndex].priority:
            return leftChildIndex
        elif leftChildIndex and rightChildIndex and self.max_heap[leftChildIndex].priority < self.max_heap[rightChildIndex].priority:
            return rightChildIndex
        return leftChildIndex if leftChildIndex else rightChildIndex

    def getHeap(self):
        return self.max_heap

    # insert will insert a node in the heap
    def insert(self, name, priority):
        self.max_heap.append(Node(name, priority))
        self.maxHeapify()

    # maxHeapify will traverse the heap in upward direction while shifting the nodes in proper places
    def maxHeapify(self, index=-1):
        index = index if index != -1 else len(self.max_heap)-1
        while index != 0:
            parentIndex = self.__getParent(index)
            if self.max_heap[parentIndex].priority >= self.max_heap[index].priority:
                break
            self.max_heap[parentIndex], self.max_heap[index] = self.max_heap[index], self.max_heap[parentIndex]
            index = parentIndex

    # extractMax will remove a node from the heap whose value will the least in the heap
    def extractMax(self):
        if len(self.max_heap) == 0:
            return None

        node = self.max_heap[0]

        # remove the first element
        self.max_heap[0] = self.max_heap[-1]
        # replace the first element with the last element
        self.max_heap = self.max_heap[:-1]
        # bubbledown the heap
        if len(self.max_heap) > 0:
            self.bubbleDown()

        return node

    # bubbleDown will traverse the heap in downward direction while shifting the nodes in proper places
    def bubbleDown(self):
        index = 0
        while index < len(self.max_heap):
            nextIndex = self.__getMaxValueChild(index)
            if not nextIndex:
                return

            if not self.max_heap[index].priority < self.max_heap[nextIndex].priority:
                break

            self.max_heap[index], self.max_heap[nextIndex] = self.max_heap[nextIndex], self.max_heap[index]
            index = nextIndex

    def remove(self, name):
        node = None

        for index in range(len(self.max_heap)):
            if self.max_heap[index].name == name:
                node = Node(name, self.max_heap[index].priority)
                self.max_heap[index].priority = float('+inf')
                self.maxHeapify(index)
        if node:
            self.extractMax()
        return node
