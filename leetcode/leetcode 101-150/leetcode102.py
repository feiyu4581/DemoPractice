# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def inorder(head, depth):
            if head:
                inorder(head.left, depth + 1)

                while depth > len(res):
                    res.append([])

                res[depth - 1].append(head.val)
                inorder(head.right, depth + 1)

        inorder(root, 1)

        return res


x = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(x.levelOrder(root) == [
    [3],
    [9,20],
    [15,7]
])
        