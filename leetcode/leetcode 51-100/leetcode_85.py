class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        row_length, col_length = len(matrix), len(matrix[0])
        left = [0 for col in range(col_length)]
        right = [col_length for col in range(col_length)]
        heights = [0 for col in range(col_length)]

        max_area = 0
        for row in range(row_length):
            cur_left, cur_right = 0, col_length
            for col in range(col_length):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0

            for col in range(col_length):
                if matrix[row][col] == '1':
                    left[col] = max(left[col], cur_left)
                else:
                    left[col] = 0
                    cur_left = col + 1

            for col in range(col_length - 1, -1, -1):
                if matrix[row][col] == '1':
                    right[col] = min(right[col], cur_right)
                else:
                    right[col] = col_length
                    cur_right = col

            for col in range(col_length):
                max_area = max(max_area, (right[col] - left[col]) * heights[col])

        return max_area
      

x = Solution()
print(x.maximalRectangle([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]) == 6)
        