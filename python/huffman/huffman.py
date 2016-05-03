#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import os.path


class HuffmanManager(object):

    def __init__(self, filename):
        with open(filename) as f:
            self.undeal_nodes = self._recompute_nodes(f)
            self.dealed_nodes = HuffmanTree()
            self.rootNode = False

    def _recompute_nodes(self, f):
        huffman_tree = HuffmanTree()
        for line in f.readlines():
            line = line.replace(' ', '')
            for char in line:
                huffman_tree.add_node(char)

        return huffman_tree


class HuffmanTree(object):
    def __init__(self, root=None, rule='min'):
        self.root = root
        self.rule = rule

    def get_node(self):
        return self.root

    def add_node(self, data):
        node = self._get_
        if not self.root:
            self.root = node
        else:
            right_deep_node = self.root.right
            while right_deep_node.right:
                right_deep_node = right_deep_node.right

            right_deep_node.right = node
            node.parent = right_deep_node

            self._ensure_node_up(node)

    def _pop_deep_node(self, node):
        res = node.right or node.left
        while res.right or res.left:
            res = res.right or res.left

        if res:
            if res.parent.right is res:
                res.parent.right = False
            else:
                res.parent.left = False

            res.parent = None

        return res

    def _swap_node_data(self, node, ensure_node):
        node.data, ensure_node.data = ensure_node.data, node.data
        node.count, ensure_node.count = ensure_node.count, node.count

    def _compare_node(self, node, another_node):
        if another_node:
            if self.rule == 'min' and another_node.count < node.count:
                return another_node

            if self.rule == 'max' and another_node.count > node.count:
                return another_node

        return node

    def _ensure_node_up(self, node):
        if node and node.parent:
            ensure_node = self._compare_node(node, node.parent)
            if ensure_node != node.parent:
                self._swap_node(node, node.parent)

            self._ensure_node(node.parent)

    def _ensure_node(self, node):
        ensure_node = node.get_ensure_node(self._compare_node)
        if ensure_node is node:
            return

        self._swap_node(node, ensure_node)
        self._ensure_node(ensure_node)

    def pop_node(self):
        deep_node = self._pop_deep_node(self.root) or self.root
        deep_node.set_children(self.root.left, self.root.right)

        res = self.root
        self.root = deep_node
        self._ensure_node(self.root)

        return res


class HuffmanNode(object):

    def __init__(self, data, count, parent=None):
        self.data = data
        self.count = count
        self.parent = parent
        self.left = False
        self.right = False

    def get_ensure_node(self, compare_node):
        node = compare_node(self, self.right)
        node = compare_node(node, self.left)

        return node

    def set_children(self, left=None, right=None):
        self.left = left
        self.right = right

        if left:
            left.parent = self
        if right:
            right.parent = self


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception(u'请输入一个需要计算的文件参数')

    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise Exception(u'输入的文件不存在')

    HuffmanManager(filename)
