class Heap:
    def __init__(self,capacity):
        self.heap = [0 for i in range(capacity)]
        self.size = 0

    def isFull(self):
        return self.size == len(self.heap)

    def getParent(self,index):
        return (index - 1) // 2

    def insert(self,value):
        if self.isFull():
            raise IndexError("Heap is full")
        self.heap[self.size] = value
        self.fixHeapAbove(self.size)
        self.size += 1

    def fixHeapAbove(self,index):
        newValue = self.heap[index]
        while index > 0 and newValue > self.getParent(index):
            self.heap[index] = self.heap[self.getParent(index)]
            index = self.getParent(index)
        self.heap[index] = newValue