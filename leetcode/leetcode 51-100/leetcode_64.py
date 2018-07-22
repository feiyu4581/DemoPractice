class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        memo = {}
        def path(row, col):
            if (row, col) not in memo:
                ans = 0
                if row + 1 < len(grid) and col + 1 < len(grid[0]):
                    ans = min(path(row + 1, col), path(row, col + 1))
                elif row + 1 < len(grid):
                    ans = path(row + 1, col)
                elif col + 1 < len(grid[0]):
                    ans = path(row, col + 1)

                memo[row, col] = grid[row][col] + ans
            return memo[row, col]

        return path(0, 0)


x = Solution()
print(x.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]) == 7)
        