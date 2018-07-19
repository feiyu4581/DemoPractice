class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        offsets = [(0, 1, cols), (1, 0, rows), (0, -1, cols), (-1, 0, rows)]

        length = min(rows % 2 == 0 and rows // 2 or rows // 2 + 1, cols % 2 == 0 and cols // 2 or cols // 2 + 1)
        for cycle in range(length):
            row, col = cycle, cycle
            res.append(matrix[row][col])
            extra = False
            for index in range(4):
                if len(res) == rows * cols:
                    return res

                offset_row, offset_col, distance = offsets[index]
                for _ in range(distance - 2 * cycle - 1):
                    row += offset_row
                    col += offset_col

                    res.append(matrix[row][col])
                    extra = True

            if extra:
                res.pop()

        return res


x = Solution()
print(x.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]) == [1,2,3,6,9,8,7,4,5])

print(x.spiralOrder([]))

print(x.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]) == [1,2,3,4,8,12,11,10,9,5,6,7])

print(x.spiralOrder([
    [1,11],
    [2,12],
    [3,13],
    [4,14],
    [5,15],
    [6,16],
    [7,17],
    [8,18],
    [9,19],
    [10,20]
]))