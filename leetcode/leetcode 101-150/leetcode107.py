# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack, res = [], []
        stack.append([root])

        while stack:
            current_val, next_nodes = [], []
            for node in stack.pop():
                if node:
                    current_val.append(node.val)
                    next_nodes.extend([node.left, node.right])

            if current_val and next_nodes:
                res.insert(0, current_val)
                stack.append(next_nodes)

        return res
        

x = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(x.levelOrderBottom(root) == [
    [15,7],
    [9,20],
    [3]
])