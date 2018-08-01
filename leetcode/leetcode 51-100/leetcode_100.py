# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def is_same(left_node, right_node):
            if not left_node and not right_node:
                return True

            left_val = left_node.val if left_node else None
            right_val = right_node.val if right_node else None

            if left_val != right_val:
                return False

            return is_same(left_node.left, right_node.left) and is_same(left_node.right, right_node.right)

        return is_same(p, q)

x = Solution()

root_1 = TreeNode(1)
root_1.left = TreeNode(2)
root_1.right = TreeNode(3)

root_2 = TreeNode(1)
root_2.left = TreeNode(2)
root_2.right = TreeNode(3)

print(x.isSameTree(root_1, root_2) == True)

root_1 = TreeNode(1)
root_1.right = TreeNode(2)

root_2 = TreeNode(1)
root_2.left = TreeNode(2)

print(x.isSameTree(root_1, root_2) == False)