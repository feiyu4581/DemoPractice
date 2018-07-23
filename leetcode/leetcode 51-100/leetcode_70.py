class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        for index in range(2, n + 1):
            dp.append(dp[index - 1] + dp[index - 2])

        return dp[n]

x = Solution()
print(x.climbStairs(2) == 2)
print(x.climbStairs(3) == 3)
        