# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        depth, stack = 1, [[root]]
        while stack:
            next_nodes = []
            for node in stack.pop():
                if not node.left and not node.right:
                    return depth

                if node.left:
                    next_nodes.append(node.left)

                if node.right:
                    next_nodes.append(node.right)

            depth += 1
            if next_nodes:
                stack.append(next_nodes)

        return depth


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
x = Solution()
print(x.minDepth(root) == 2)
        