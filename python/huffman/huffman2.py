from collections import namedtuple
import random

class Node(object):
    def __init__(self, key, value, leaf=False):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.leaf = leaf

    def __repr__(self):
        return '[NODE]%s' % self.value

    def walk(self, prefix=''):
        if not self.left and not self.right:
            print (self.value, prefix)
        else:
            if self.left:
                self.left.walk(prefix=prefix + '0')
            if self.right:
                self.right.walk(prefix=prefix + '1')

class MinHeapQueue:
    def __init__(self, compare=None):
        self.queues = [None]
        self.compare = compare or (lambda x, y: x <= y)
        self.heap_size = 0

    def left(self, index):
        return index * 2

    def right(self, index):
        return index * 2 + 1

    def parent(self, index):
        return int(index / 2)

    def justify_reversed(self, index):
        parent_index = self.parent(index)
        while index > 1 and self.compare(self.queues[index], self.queues[parent_index]):
            self.queues[parent_index], self.queues[index] = self.queues[index], self.queues[parent_index]
            index, parent_index = parent_index, self.parent(parent_index)

    def init(self, queues):
        self.queues = [None] + queues
        self.heap_size = len(queues)

        for index in range(self.parent(self.heap_size), 0, -1):
            self.justify(index)

    def justify(self, index):
        left, right = self.left(index), self.right(index)
        minmum = index
        if left <= self.heap_size and self.compare(self.queues[left], self.queues[minmum]):
            minmum = left

        if right <= self.heap_size and self.compare(self.queues[right], self.queues[minmum]):
            minmum = right

        if minmum != index:
            self.queues[index], self.queues[minmum] = self.queues[minmum], self.queues[index]
            self.justify(minmum)

    def insert(self, node):
        self.heap_size += 1
        if self.heap_size == len(self.queues):
            self.queues.append(node)
        else:
            self.queues[self.heap_size] = node

        self.justify_reversed(self.heap_size)

    def pop(self):
        if self.heap_size == 0:
            raise AttributeError('Empty Queue')

        self.queues[1], self.queues[self.heap_size] = self.queues[self.heap_size], self.queues[1]
        self.heap_size -= 1
        self.justify(1)

        return self.queues[self.heap_size + 1]

    def __len__(self):
        return self.heap_size


values = [
    ('A', 0.2),
    ('B', 0.3),
    ('C', 0.11),
    ('D', 0.4),
    ('E', 0.3),
    ('F', 0.22)
]

nodes = [Node(value[1], value[0], leaf=True) for value in values]
queue = MinHeapQueue(compare=lambda left, right: left.key <= right.key)
queue.init(nodes)

while len(queue) >= 2:
    left, right = queue.pop(), queue.pop()
    parent = Node(left.key + right.key, None)
    left.parent, right.parent = parent, parent
    parent.left, parent.right = left, right

    queue.insert(parent)

root = queue.pop()


root.walk()