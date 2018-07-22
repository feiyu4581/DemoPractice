class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}
        def path(row, col):
            nonlocal memo
            if (row, col) not in memo:
                ans = 0
                if row > 1 and col > 1:
                    ans = path(row - 1, col) + path(row, col - 1) + 1

                memo[row, col] = ans

            return memo[row, col]
        
        return path(m, n) + 1

x = Solution()
print(x.uniquePaths(3, 2) == 3)
print(x.uniquePaths(7, 3) == 28)
        