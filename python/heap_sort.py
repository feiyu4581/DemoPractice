# -*- encoding: utf-8 -*-


class Heap(object):
    def __init__(self, value):
        self.size = len(value)

        value.insert(0, 0)
        self.value = value
        # self.default_compare = self.default_sort

    def default_sort(self, left, right):
        if left > self.size or right < 1:
            return False

        return self.value[left] > self.value[right]

    def reduce_size(self):
        self.size -= 1

    def parent(self, index):
        return index / 2

    def left(self, index):
        return index * 2

    def right(self, index):
        return index * 2 + 1

    def swap(self, left, right):
        self.value[left], self.value[right] = self.value[right], self.value[left]

    def heapify(self, index):
        if index < 1 or index > self.size:
            return

        old_index = index
        if self.default_sort(self.left(index), index):
            index = self.left(index)

        if self.default_sort(self.right(old_index), index):
            index = self.right(old_index)

        if index != old_index:
            self.swap(index, old_index)
            self.heapify(index)

    def heap(self):
        for index in xrange(self.size / 2, 0, -1):
            self.heapify(index)

    def heap_sort(self):
        for index in xrange(self.size, 0, -1):
            self.swap(index, 1)
            self.reduce_size()
            self.heapify(1)


import random
h = Heap([random.randint(1, 100) for i in range(10)])
print 'original      :', h.value

h.heap()
print 'heaped        :', h.value

h.heap_sort()
print 'heap_srot     :', h.value
