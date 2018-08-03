# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def generate_node(cls, vals):
        root, current = None, None
        for val in vals:
            node = cls(val)
            if not root:
                root = node

            if current:
                current.next = node

            current = node

        return root

    @staticmethod
    def printof(head):
        current = head
        while current:
            print (current.val)
            current = current.next

    def __repr__(self):
        vals = []
        current = self
        while current:
            vals.append(current.val)
            current = current.next

        return '<ListNode {}>'.format(vals)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def to_bst(root, index):
            if not root or index <= 0:
                return None, root

            if index == 1:
                return TreeNode(root.val), root.next

            mid = index // 2 + index % 2
            left_node, node = to_bst(root, mid - 1)
            root = TreeNode(node.val)

            root.left = left_node
            root.right, next_node = to_bst(node.next, index - mid)

            return root, next_node

        index, current = 0, head
        while current:
            index += 1
            current = current.next

        root, _ = to_bst(head, index)

        return root


x = Solution()

print(x.sortedListToBST(ListNode.generate_node([-10, -3, 0, 5, 9])))