# -*- encoding: utf-8 -*-
import random


class Tree(object):
    def __init__(self):
        self.root = False

    def insert(self, value, root=False):
        if not self.root:
            self.root = TreeNode(value)
            return

        root = root or self.root
        if root.value >= value:
            if root.left:
                self.insert(value, root.left)
            else:
                root.setLeft(TreeNode(value))
        else:
            if root.right:
                self.insert(value, root.right)
            else:
                root.setRight(TreeNode(value))

    def iterRoot(self, root=False):
        if root:
            self.iterRoot(root.left)
            print root.value
            self.iterRoot(root.right)


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = False
        self.right = False

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right


x = Tree()
for i in range(10):
    x.insert(random.randint(1, 100))

x.iterRoot(x.root)
