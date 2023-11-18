
import math
from QueueNode import QueueNode


class PriorityMinQueue:
    size = 0
    queue = []
    handles = {}

    def __init__(self, size, queue, handles):
        self.size = size
        self.queue = queue
        self.handles = handles

    def delete_min(self) -> QueueNode:

        if self.size == 1:
            min = self.queue[0]
            self.size = self.size-1
            return min
        else:
            min = self.queue[0]
            self.queue[0] = self.queue[self.size-1]
            self.size = self.size-1
            self.heap_down(0)
            self.handles.pop(min.node)
            return min

    def heap_down(self, index):
        leftIndex = 2*index+1
        rightIndex = 2*index+2

        if not (leftIndex > self.size and rightIndex > self.size):
            indexMin = index
            if leftIndex < self.size and self.queue[leftIndex].key < self.queue[indexMin].key:
                indexMin = leftIndex
            if rightIndex < self.size and self.queue[rightIndex].key < self.queue[indexMin].key:
                indexMin = rightIndex
            if index != indexMin:
                temp = self.queue[index]
                self.queue[index] = self.queue[indexMin]
                self.queue[indexMin] = temp

                self.handles.update({self.queue[index].node: index})
                self.handles.update({self.queue[indexMin].node: indexMin})
                self.heap_down(indexMin)


    def heap_up(self, index):

        while (index-1)/2 >= 0 and index > 0:
            parent =math.floor((index-1)/2) 

            if self.queue[index].key < self.queue[parent].key:
                temp = self.queue[index]
                self.queue[index] = self.queue[parent]
                self.queue[parent] = temp

                self.handles[self.queue[index].node]=index
                self.handles[self.queue[parent].node] =parent

                index = parent
            else:
                break

    def getMin(self)-> QueueNode:
        return self.queue[0]
