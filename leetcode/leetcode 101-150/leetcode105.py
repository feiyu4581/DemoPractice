# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(pres, ins):
            if not pres or not ins:
                return None

            root = TreeNode(pres.pop(0))
            index = ins.index(root.val)

            root.left = build(pres, ins[:index])
            root.right = build(pres, ins[index+1:])

            return root

        return build(preorder, inorder)


x = Solution()
# res = x.buildTree([3,9,20,15,7], [9,3,15,20,7])
res = x.buildTree([1,4,2,3], [1,2,3,4])

# print([res.left.val, res.right.left.val, res.right.val, res.val, res.right.right.val])
        