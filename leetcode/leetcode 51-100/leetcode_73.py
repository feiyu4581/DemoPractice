class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix

        row_len, col_len = len(matrix), len(matrix[0])
        length = max(row_len, col_len)
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    for index in range(length):
                        if index < row_len and matrix[index][col] != 0:
                            matrix[index][col] = None
                        
                        if index < col_len and matrix[row][index] != 0:
                            matrix[row][index] = None

        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] is None:
                    matrix[row][col] = 0

        return matrix


x = Solution()
# print(x.setZeroes([
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]) == [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ])

print(x.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]) == [
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
])
