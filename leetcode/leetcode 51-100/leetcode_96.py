class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def generate(low, high):
            if low >= high:
                return 1
            else:
                if (low, high) not in memo:
                    res = 0
                    for index in range(low, high + 1):
                        res += generate(low, index - 1) * generate(index + 1, high)

                    memo[low, high] = res

                return memo[low, high]

        if n <= 0:
            return 0

        return generate(1, n)



x = Solution()
# print(x.numTrees(3) == 5)
print(x.numTrees(4))
        