# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def path_sum(head, pre_num):
            if not head:
                return False

            if not head.left and not head.right and head.val + pre_num == sum:
                return True

            return path_sum(head.left, pre_num + head.val) or path_sum(head.right, pre_num + head.val)

        return path_sum(root, 0)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
x = Solution()
print(x.hasPathSum(root, 38) == True)
                