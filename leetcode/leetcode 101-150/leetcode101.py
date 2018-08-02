# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        stack = [(root, root)]
        while stack:
            left, right = stack.pop()
            if left and right:
                if left.val != right.val:
                    return False

                if left and right:
                    stack.append((left.left, right.right))
                    stack.append((left.right, right.left))
            elif left or right:
                return False

        return True

    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_symmetric(left, right):
            if not left and not right:
                return True

            left_value = left.val if left else None
            right_value = right.val if right else None

            if left_value != right_value:
                return False

            return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)

        return is_symmetric(root, root)


x = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(x.isSymmetric(root) == True)
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print(x.isSymmetric(root) == False)
        