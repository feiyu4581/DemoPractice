# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_depth = 0
        def inorder(head, depth):
            nonlocal max_depth
            if head:
                inorder(head.left, depth + 1)
                max_depth = max(max_depth, depth)
                inorder(head.right, depth + 1)

        inorder(root, 1)
        return max_depth


x = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(x.maxDepth(root) == 3)