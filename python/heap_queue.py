import math


class HeapQueue(object):
    def __init__(self, array):
        self.max_queue = len(array)
        self.array = [''] + array

    def parent(self, index):
        return self.array[int(math.floor(index / 2))]

    def left(self, index):
        if index * 2 > self.max_queue:
            raise IndexError('Out of range')

        return self.array[index * 2]

    def right(self, index):
        if index * 2 + 1 > self.max_queue:
            raise IndexError('Out of range')

        return self.array[index * 2 + 1]

    def max_heapify(self, index):
        if index > self.max_queue:
            raise IndexError('Out of range')

        pass
