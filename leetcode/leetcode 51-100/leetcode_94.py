# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def traversal(head):
            nonlocal res
            if head:
                traversal(head.left)
                res.append(head.val)
                traversal(head.right)

        traversal(root)
        return res

    def inorderTraversal(self, root):
        res, stack = [], []

        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                if node.right:
                    stack.append(node.right)
                stack.append(node.val)
                if node.left:
                    stack.append(node.left)
            else:
                res.append(node)

        return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
        
x = Solution()
print(x.inorderTraversal(root))