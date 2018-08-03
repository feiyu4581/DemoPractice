# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build(ins, posts):
            if not ins or not posts:
                return None

            root = TreeNode(posts[-1])
            index = ins.index(root.val)

            root.left = build(ins[:index], posts[:index])
            root.right = build(ins[index + 1:], posts[index:-1])

            return root

        return build(inorder, postorder)

    
x = Solution()
res = x.buildTree([9,3,15,20,7], [9,15,7,20,3])

print (res.val, res.left.val, res.right.val, res.right.left.val, res.right.right.val)