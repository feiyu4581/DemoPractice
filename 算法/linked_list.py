import random

class Node(object):
    '''
    链表节点
    '''
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None

    def equals(self, val):
        return self.val == val


class LinkedList(object):
    '''
    双向链表使用，支持以下方法
    @find：查询
    @insert：插入
    @append：追加
    @remove：移除
    @pop：弹出
    '''

    def __init__(self):
        self.header = Node(None)
        self.tail = self.header

    def get_header(self):
        return self.header.next

    def traverse(self):
        current = self.get_header()
        while current:
            yield current
            current = current.next

    def find(self, val):
        for node in self.traverse():
            if node.equals(val):
                return node

        return None

    def append(self, val):
        self.tail.next = Node(val)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next

        return self.tail

    def insert_before(self, node, val):
        if not node:
            raise AttributeError('Empty Node')

        new_node = Node(val)
        new_node.next = node
        new_node.previous = node.previous

        node.previous.next = new_node
        node.previous = new_node

        return new_node

    def insert_after(self, node, val):
        if not node:
            raise AttributeError('Empty Node')

        new_node = Node(val)
        new_node.next = node.next
        new_node.previous = node

        if node.next:
            node.next.previous = new_node
        else:
            self.tail = new_node

        node.next = new_node
        return new_node

    def remove(self, node):
        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.previous.next = node.next
        del node

    def pop(self):
        if self.header is self.tail:
            raise KeyError('Empty List')

        node = self.tail
        self.tail = node.previous
        self.tail.next = None

        return node

    def show(self):
        nodes = []
        current = self.get_header()
        while current:
            nodes.append(current.val)
            current = current.next

        print(f'nodes={nodes}, header={self.get_header().val}, tail={self.tail.val}')

    def reverse(self):
        '''
        链表反转
        '''
        current = self.get_header()
        last_node = None
        while current.next:
            next_node = current.next
            next_node.previous = next_node.next

            current.previous = next_node
            current.next = last_node

            last_node = current
            current = next_node

        self.tail = self.header.next
        self.tail.next = None

        current.next = last_node
        self.header.next = current

    def check_cycle(self):
        '''
        环的检测
        '''
        # 每次只前进一格
        current = self.get_header().next
        if not current.next:
            return False

        # 每次前进两格
        double_current = current.next

        # count 每次增加的时候 double_current 都迁移一位，current 只在增加两次的时候迁移一次
        # 这样 double_current 遍历速度是 current 的两倍，当存在环的时候，double_current 必将
        # 再次追上 current，如果没有追上表示不存在环，并且必定在 current 到达 tail 的时候再次追上
        count = 1
        while current.next and double_current.next:
            if current is double_current:
                return True

            double_current = double_current.next
            if count % 2 == 0:
                current = current.next

            count += 1

        return False

    @staticmethod
    def merge(left, right):
        '''
        有序链表合并
        '''
        res = LinkedList()
        left_node = left.get_header()
        right_node = right.get_header()

        while left_node or right_node:
            if left_node and right_node:
                if left_node.val > right_node.val:
                    append_node = right_node
                else:
                    append_node = left_node
            elif left_node:
                append_node = left_node
            else:
                append_node = right_node

            res.append(append_node.val)
            if append_node is left_node:
                left_node = left_node.next
            else:
                right_node = right_node.next

        return res

    def unlink_reverse(self, n):
        '''
        删除链表倒数第 n 个节点
        '''
        def recursive_reverse(node, index):
            if node.next:
                res_node, index = recursive_reverse(node.next, index)
                if res_node:
                    return res_node, index

                index = index + 1
            else:
                index = index + 1

            if index == n:
                return node, index
            else:
                return None, index

        node, index = recursive_reverse(self.get_header(), 0)
        self.remove(node)
        return index

    def middle(self):
        '''
        求链表的中间节点
        '''
        current = self.header
        double_current = self.header

        while current.next and double_current.next and double_current.next.next:
            current = current.next
            double_current = double_current.next.next

        if not double_current.next:
            if not current.next:
                return 0

            return (current.val + current.next.val) / 2
        else:
            return current.next.val


    @staticmethod
    def test():
        linked_list = LinkedList()
        for i in range(1, 10):
            linked_list.append(i)

        linked_list.show()
        node = linked_list.find(5)
        print(node.val)
        linked_list.insert_after(node, 15)
        linked_list.insert_before(node, 25)
        linked_list.show()


    @staticmethod
    def test2():
        linked_list = LinkedList()
        for i in range(10):
            linked_list.append(i)

        linked_list.show()
        linked_list.reverse()
        linked_list.show()

        print(linked_list.check_cycle())
        node = linked_list.find(5)
        node.previous = linked_list.tail
        linked_list.tail.next = node
        print(linked_list.check_cycle())

        left = LinkedList()
        right = LinkedList()

        for i in range(20):
            if random.randint(1, 10) > 5:
                left.append(i)
            else:
                right.append(i)

        left.show()
        right.show()

        merege_list = LinkedList.merge(left, right)
        merege_list.show()

        print(merege_list.middle())
        merege_list.unlink_reverse(1)
        merege_list.show()
        print(merege_list.middle())


if __name__ == "__main__":
    # LinkedList.test()
    LinkedList.test2()
