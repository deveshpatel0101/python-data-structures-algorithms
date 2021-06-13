from queues.priority_queue.heap import MaxHeap


class PriorityQueue:
    def __init__(self):
        self.priority_queue = MaxHeap()

    def insert(self, name, priority):
        self.priority_queue.insert(name, priority)

    def remove(self):
        return self.priority_queue.extractMax()

    def display(self):
        return self.priority_queue.getHeap()
