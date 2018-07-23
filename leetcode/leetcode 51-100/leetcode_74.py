class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row_len, col_len = len(matrix), len(matrix[0])
        start, end = (0, 0), (row_len - 1, col_len - 1)
        while start <= end:
            mid = (start[0] * col_len + start[1] + end[0] * col_len + end[1]) // 2
            row, col = mid // col_len, mid % col_len

            if matrix[row][col] == target:
                return True

            if matrix[row][col] < target:
                if col + 1 >= col_len:
                    start = (row + 1, 0)
                else:
                    start = (row, col + 1)
            else:
                if col - 1 < 0:
                    end = (row - 1, col_len - 1)
                else:
                    end = (row, col - 1)

        return False


x = Solution()
print(x.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3) == True)
        
print(x.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 13) == False)
