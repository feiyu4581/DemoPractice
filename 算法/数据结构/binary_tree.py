import random


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def compare(self, val):
        if self.val == val:
            return 0

        return -1 if self.val > val else 1

    def __str__(self):
        return f'Node(val={self.val})'


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def find(self, val):
        # 节点查询
        current = self.root
        while current:
            if current.compare(val) == 0:
                return current
            elif current.compare(val) < 0:
                current = current.left
            else:
                current = current.right

        return None

    def min(self, node):
        # 返回最小节点
        while node.left:
            node = node.left

        return node

    def max(self, node):
        # 返回最大节点
        while node.right:
            node = node.right

        return node

    def previous(self, node):
        # 返回节点的前驱
        if node.left:
            return self.max(node.left)

        while node.parent and node.parent == node.parent.left:
            node = node.parent

        return node.parent

    def next(self, node):
        # 返回节点的后驱
        if node.right:
            return self.min(node.right)

        while node.parent and node.parent == node.parent.right:
            node = node.parent

        return node.parent

    def _inorder_recursive(self, node):
        # 中序遍历
        if node:
            self._inorder_recursive(node.left)
            print(node)
            self._inorder_recursive(node.right)

    def inorder_recursive(self):
        self._inorder_recursive(self.root)

    def inorder(self):
        # 中序遍历，使用顺序遍历
        nodes = []
        stack = [self.root]
        visited = set()
        while stack:
            node = stack.pop()
            if not node:
                continue

            if node in visited:
                nodes.append(node)
            else:
                visited.add(node)
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)

        print(','.join(map(str, nodes)))

    def insert(self, val):
        # 插入节点
        current = self.root
        parent = None
        # 寻找插入节点的位置
        while current:
            parent = current
            if current.compare(val) <= 0:
                current = current.left
            else:
                current = current.right

        node = TreeNode(val)
        node.parent = parent
        if parent is None:
            self.root = node
        elif parent.compare(val) <= 0:
            parent.left = node
        else:
            parent.right = node

        return node

    def transplant(self, dst, target):
        # 使用 dst 坐在的数来替换 target所在的数
        if not target.parent:
            self.root = dst
        elif target.parent.left == target:
            target.parent.left = dst
        else:
            target.parent.right = dst

        if dst:
            dst.parent = target.parent

    def unlink(self, node):
        next_node = None
        if node.left and node.right:
            # 对于两个节点都存在的场景，先找到当前节点的后驱节点
            next_node = self.next(node)
            # 如果后驱节点不是节点的右边节点，那么一定是右边节点的最左边节点
            if next_node != node.right:
                # 使用这个节点的右边节点替换当前节点（只可能有右边节点，如果存在左边节点，它就不是后驱节点了，因为存在更小的节点）
                self.transplant(next_node.right, next_node)
                # 将这个后驱节点移动到要删除节点的右边节点，原来的右边节点作为它的直接点
                next_node.right = node.right
                node.right.parent = next_node

            # 使用右边节点来替换当前节点
            self.transplant(next_node, node)
            next_node.left = node.left
            node.left.parent = next_node
        else:
            # 如果只有一个子节点或者没有子节点，那么直接使用这个节点来替换当前节点
            self.transplant(node.left or node.right, node)

        del node


if __name__ == '__main__':
    tree = BinaryTree()
    nums = []
    for i in range(100):
        num = random.randint(1, 100)
        tree.insert(num)

        if random.randint(1, 50) > 25:
            nums.append(num)

    for index, num in enumerate(nums):
        node = tree.find(num)
        tree.unlink(node)

    tree.inorder()
