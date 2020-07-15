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
        while index > 0 and newValue > self.heap[self.getParent(index)]:
            self.heap[index] = self.heap[self.getParent(index)]
            index = self.getParent(index)
        self.heap[index] = newValue

    def fixHeapBelow(self,index,lastHeapIndex):
        childToSwap = None

        while index <= lastHeapIndex:
            leftChild = self.getChild(index)
            rightChild = self.getChild(index,False)
            if leftChild <= lastHeapIndex:
                if rightChild > lastHeapIndex:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild
                if self.heap[index] < self.heap[childToSwap]:
                    tmp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = tmp
                else:
                    break

                index = childToSwap

            else:
                break


    def isEmpty(self):
        return self.size == 0

    def getChild(self,index,left=True):
        a = 0
        if left:
            a = 1
        else:
            a = 2
        return 2 * index + a

    def delete(self,index):
        if self.isEmpty():
            raise IndexError("Heap is empty")

        parent = self.getParent(index)
        deletedValue = self.heap[index]

        self.heap[index] = self.heap[self.size - 1]

        if index == 0 or self.heap[index] < self.heap[parent]:
            self.fixHeapBelow(index,self.size - 1)
        else:
            self.fixHeapAbove(index)

        self.size -= 1
        return deletedValue

    def printHeap(self):
        for i in range(self.size):
            print(self.heap[i],end=", ")
        print()

if __name__ == "__main__":
    heap = Heap(10)
    heap.insert(80)
    heap.insert(75)
    heap.insert(60)
    heap.insert(68)
    heap.insert(55)
    heap.insert(40)
    heap.insert(52)
    heap.insert(67)

    heap.printHeap()