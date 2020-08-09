
class Array(object):
    '''
    数组使用，支持以下方法
    @find：查询
    @insert：插入
    @append：追加
    @remove：移除
    @pop：弹出
    '''
    MIN_CAPICITY = 20

    def __init__(self, capicity=MIN_CAPICITY):
        self.length = 0
        self.size = max(capicity, self.MIN_CAPICITY)
        self.vector = [None] * self.size

    def find(self, target):
        for index in range(0, self.length):
            if self.vector[index] == target:
                return index

        return -1

    def check_capicity(self):
        # 当空间不足的时候，创建一个更大的空间，将过去的数据复制过去
        if self.length == self.size:
            self.size = self.size * 2 + 1
            old_vector = self.vector
            self.vector = [None] * self.size
            for index in range(0, self.length):
                self.vector[index] = old_vector[index]

            del old_vector

    def append(self, val):
        self.check_capicity()
        self.vector[self.length] = val
        self.length += 1
        return self.length - 1
 
    def insert(self, index, val):
        if index >= self.length or index < 0:
            raise KeyError('Unbound Error')

        self.check_capicity()
        for index in range(self.length, index, -1):
            self.vector[index] = self.vector[index - 1]

        self.vector[index] = val
        self.length += 1
        return index

    def remove(self, val):
        index = self.find(val)
        if index < 0:
            return -1

        for index in range(index, self.length - 1):
            self.vector[index] = self.vector[index] + 1

        self.length -= 1
        return index

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