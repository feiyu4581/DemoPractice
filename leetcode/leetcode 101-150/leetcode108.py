# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def to_bst(low, high):
            if low > high:
                return None

            mid = (low + high) // 2
            root = TreeNode(nums[mid])
            root.left = to_bst(low, mid - 1)
            root.right = to_bst(mid + 1, high)

            return root

        return to_bst(0, len(nums) -1)


x = Solution()
res = x.sortedArrayToBST([-10,-3,0,5,9])

print (res)