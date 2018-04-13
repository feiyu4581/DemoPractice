# -*- encoding: utf-8 -*-
import random
from collections import namedtuple


class Node(object):
    def __init__(self, parent, key, value):
        self.parent = parent
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '[NODE]%s' % self.value

class Tree(object):
    def __init__(self):
        self.root = False

    def _inorder_walk(self, node):
        res = []
        if node:
            res.extend(self._inorder_walk(node.left))
            res.append(node)
            res.extend(self._inorder_walk(node.right))

        return res

    def _reverse_inorder_walk(self, node):
        res = []
        if node:
            res.extend(self._reverse_inorder_walk(node.right))
            res.append(node)
            res.extend(self._reverse_inorder_walk(node.left))

        return res

    def inorder_walk(self):
        return self._inorder_walk(self.root)

    def reverse_order_walk(self):
        return self._reverse_inorder_walk(self.root)

    def _search(self, node, key):
        if not node:
            return -1

        if node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def maxmum(self, node=None):
        node = node or self.root

        while node and node.right:
            node = node.right

        return node
        
    def minmum(self, node=None):
        node = node or self.root

        while node and node.left:
            node = node.left

        return node

    def predecessor(self, node):
        if not node:
            return None

        if node.left:
            return self.maxmum(node.left)

        while node.parent and node.parent.left == node:
            node = node.parent

        return node.parent


    def successor(self, node):
        if not node:
            return None

        if node.right:
            return self.minmum(node.right)

        while node.parent and node.parent.right == node:
            node = node.parent

        return node.parent

    def insert(self, key, value):
        node = Node(None, key, value)
        if not self.root:
            self.root = node
        else:
            current = self.root
            parent = None
            while current:
                parent = current
                if node.key < current.key:
                    current = current.left
                else:
                    current = current.right

            if node.key < parent.key:
                parent.left = node
            else:
                parent.right = node

            node.parent = parent

    def resursive_insert(self, key, value, root=None):
        if not self.root:
            self.root = Node(None, key, value)
        else:
            current = root or self.root
            if key < current.key:
                if current.left:
                    self.resursive_insert(key, value, current.left)
                else:
                    current.left = Node(current.left, key, value)
            else:
                if current.right:
                    self.resursive_insert(key, value, current.right)
                else:
                    current.right = Node(current.right, key, value)

    def transplant(self, node, replace_node):
        if not node.parent:
            self.root = replace_node
        elif node.parent.left == node:
            node.parent.left = replace_node
        else:
            node.parent.right = replace_node

        if replace_node and node.parent:
            replace_node.parent = node.parent

    def delete(self, node):
        if not node.left:
            self.transplant(node, node.right)
        elif not node.right:
            self.transplant(node, node.left)
        else:
            next_node = self.successor(node)
            if next_node.parent != node:
                self.transplant(next_node, next_node.right)
                next_node.right = node.right
                next_node.parent = node
            self.transplant(node, next_node)
            next_node.left = node.left
            node.left.parent = next_node


tree = Tree()
for i in range(10):
    key = random.randint(1, 100)
    tree.insert(key, key)

print tree.inorder_walk()
