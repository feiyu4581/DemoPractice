# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        memo = {}
        def generate(low, high):
            if low > high:
                return [None]
            if low == high:
                return [TreeNode(low)]
            else:
                if (low, high) not in memo:
                    res = []
                    for index in range(low, high + 1):
                        for left_node in generate(low, index - 1):
                            for right_node in generate(index + 1, high):
                                new_node = TreeNode(index)
                                new_node.left = left_node
                                new_node.right = right_node

                                res.append(new_node)

                    memo[low, high] = res
                return memo[low, high]

        if n <= 0:
            return []

        return generate(1, n)
        


x = Solution()
print(x.generateTrees(3))
        