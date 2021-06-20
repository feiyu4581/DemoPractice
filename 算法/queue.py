from linked_list import LinkedList
MIN_CAPACITY = 20


class LinkedListDeque(object):
    def __init__(self, capacity=MIN_CAPACITY):
        self.size = capacity
        self.deque = LinkedList()

    def dequeue(self, val):
        if self.deque.size >= self.size:
            raise ValueError("Index out of deque")

        self.deque.append(val)

    def enqueue(self):
        if self.deque.size == 0:
            raise ValueError("Empty queue")

        return self.deque.pop().val

    def dequeue_right(self, val):
        self.dequeue(val)

    def enqueue_right(self):
        return self.enqueue()

    def dequeue_left(self, val):
        if self.deque.size >= self.size:
            raise ValueError("Index out of deque")

        self.deque.insert_before(self.deque.get_header(), val)

    def enqueue_left(self):
        if self.deque.size == 0:
            raise ValueError("Empty queue")

        val = self.deque.get_header().val
        self.deque.remove(self.deque.get_header())

        return val


class ArrayListDeque(object):
    """
    循环数组来作为一个队列
    """
    def __init__(self, capacity=MIN_CAPACITY):
        self.size = capacity
        self.left, self.right, self.length = 0, 0, 0
        self.array = [None] * self.size

    def dequeue(self, val):
        if self.length >= self.size:
            raise ValueError("Index out of deque")

        self.array[self.right % self.size] = val
        self.right += 1
        self.length += 1

    def enqueue(self):
        if self.length == 0:
            raise ValueError("Empty queue")

        self.right -= 1
        self.length -= 1

        return self.array[self.right % self.size]

    def dequeue_right(self, val):
        self.dequeue(val)

    def enqueue_right(self):
        return self.enqueue()

    def dequeue_left(self, val):
        if self.length >= self.size:
            raise ValueError("Index out of deque")

        self.array[(self.left - 1) % self.size] = val
        self.left -= 1
        self.length += 1

    def enqueue_left(self):
        if self.length == 0:
            raise ValueError("Empty queue")

        self.left += 1
        self.length -= 1

        return self.array[(self.left - 1) % self.size]


if __name__ == '__main__':
    deque = ArrayListDeque()

    for i in range(10):
        deque.dequeue_left(i)

    print(deque.array)
    print(deque.enqueue())
    print(deque.enqueue())

    print(deque.left)
    print(deque.enqueue_left())
    print(deque.enqueue_left())

    deque.dequeue_left(100)

    print(deque.array)
