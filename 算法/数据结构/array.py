
class Array(object):
    """
    数组使用，支持以下方法
    @find：查询
    @insert：插入
    @append：追加
    @remove：移除
    @pop：弹出
    """
    MIN_CAPACITY = 20

    def __init__(self, capacity=MIN_CAPACITY):
        self.length = 0
        self.size = max(capacity, self.MIN_CAPACITY)
        self.vector = [None] * self.size

    def find(self, target):
        for i in range(0, self.length):
            if self.vector[i] == target:
                return i

        return -1

    def check_capacity(self):
        # 当空间不足的时候，创建一个更大的空间，将过去的数据复制过去
        if self.length == self.size:
            self.size = self.size * 2 + 1
            old_vector = self.vector
            self.vector = [None] * self.size
            for i in range(0, self.length):
                self.vector[i] = old_vector[i]

            del old_vector

    def append(self, val):
        self.check_capacity()
        self.vector[self.length] = val
        self.length += 1
        return self.length - 1
 
    def insert(self, position, val):
        if position >= self.length or position < 0:
            raise KeyError('Unbound Error')

        self.check_capacity()
        for i in range(self.length, position, -1):
            self.vector[i] = self.vector[i - 1]

        self.vector[position] = val
        self.length += 1
        return position

    def remove(self, val):
        position = self.find(val)
        if position < 0:
            return -1

        for i in range(position, self.length - 1):
            self.vector[i] = self.vector[i + 1]

        self.length -= 1
        return position

    def pop(self):
        if self.length == 0:
            raise KeyError('Empty Array')

        self.length -= 1
        return self.vector[self.length]

    def show(self):
        print(f'Length={self.length}, Size={self.size}, Vector={self.vector[:self.length]}')


if __name__ == "__main__":
    array = Array()
    for index in range(0, 30):
        array.append(index)

    array.insert(10, 50)
    array.remove(12)
    print(array.pop())
    array.show()
