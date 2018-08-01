# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(head, low, high):
            if not head:
                return True

            if head.val <= low or head.val >= high:
                return False

            return valid(head.left, low, head.val) and valid(head.right, head.val, high)

        return valid(root, float('-inf'), float('inf'))


x = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(x.isValidBST(root) == True)
        
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(x.isValidBST(root) == False)