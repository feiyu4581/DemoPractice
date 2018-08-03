# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balance(node, index):
            if not node:
                return index - 1

            left_index = balance(node.left, index + 1)
            right_index = balance(node.right, index + 1)

            if left_index > 0 and right_index > 0 and abs(left_index - right_index) <= 1:
                return max(left_index, right_index)
            else:
                return -1

        return balance(root, 1) != -1


x = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(7)
print (x.isBalanced(root) == True)
        