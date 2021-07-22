import random

MAX_LEVEL = 16


class Node(object):
    def __init__(self, val, max_level=MAX_LEVEL):
        self.val = val
        self.next = [None] * max_level

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return repr(self.val)


class SkipList(object):
    def __init__(self):
        self.header = Node(None)
        self.current_level = 1

    @staticmethod
    def get_level():
        level = 1
        # 按照概率来计算层次，每次存在 50% 概率来添加一个层次
        while random.randint(1, 10) > 5 and level < MAX_LEVEL:
            level += 1

        return level

    def find_previous(self, val):
        current = self.header
        previous_lists = [None] * self.current_level
        for i in range(self.current_level - 1, -1, -1):
            while current.next[i] and current.next[i].val < val:
                current = current.next[i]

            # 找到指定节点的所有前置节点，也就是跳表里面每一层最接近给定值的节点
            previous_lists[i] = current

        return previous_lists

    def find(self, val):
        previous = self.find_previous(val)[0]
        # 如果最后一个节点的下一个节点是指定值，那么认为找到给定值
        if previous.next[0] and previous.next[0].val == val:
            return previous.next[0]

        return None

    def insert(self, val):
        level = self.get_level()
        # 动态生成层数
        if level > self.current_level:
            self.current_level = level

        previous_lists = self.find_previous(val)
        node = Node(val, level)
        # 将所有前置节点执行当前节点，当前节点执行下一个节点，只判断指定层次的数据，更高层次的数据保留原有数据
        for i in range(level):
            node.next[i] = previous_lists[i].next[i]
            previous_lists[i].next[i] = node

        return node

    def unlink(self, val):
        previous_lists = self.find_previous(val)
        node = self.find(val)
        if not node:
            return -1

        for i, previous in enumerate(previous_lists):
            # 将当前节点从每一层的链表中删除掉
            if i < len(node.next):
                previous.next[i] = node.next[i]
                node.next[i] = None

        del node

    def get_nodes(self):
        current_node = self.header

        layers = []
        while current_node.next[0]:
            layers.append(current_node.next[0])
            current_node = current_node.next[0]

        return layers

    def show(self):
        layers = self.get_nodes()
        for i in range(self.current_level - 1, -1, -1):
            current_node = self.header.next[i]
            row = []
            for node in layers:
                if current_node is node:
                    row.append(node.val)
                    current_node = current_node.next[i]
                else:
                    row.append('-')

            print(','.join(map(lambda column: '{:>3}'.format(column), row)))


if __name__ == '__main__':
    skip_list = SkipList()
    res = []
    for i in range(50):
        num = random.randint(1, 100)
        res.append(num)

        skip_list.insert(num)

    skip_list.show()

    print(skip_list.get_nodes())

    for num in res:
        print(skip_list.find(num))
        skip_list.unlink(num)

    print(skip_list.get_nodes())
