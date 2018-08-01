# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pre, first, second = None, None, None
        def inorder(head):
            nonlocal pre, first, second
            if not head:
                return
                
            inorder(head.left)
            
            if pre and pre.val > head.val:
                if not first:
                    first = pre

                second = head

            pre = head
            inorder(head.right)

        if root:
            inorder(root)
            first.val, second.val = second.val, first.val
            
        return root


root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)

x = Solution()
res = x.recoverTree(root)
print([res.val, res.left.val, res.right.val])
        