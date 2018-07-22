class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []

        index = 1
        cycles = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[0] * n for _ in range(n)]

        length = n % 2 == 0 and n // 2 or n // 2 + 1
        for layer in range(length):
            row, col = layer, layer
            res[row][col] = index
            index += 1
            for cycle in range(4):
                row_offset, col_offset = cycles[cycle]
                for _ in range(n - 2 * layer - 1):
                    row += row_offset
                    col += col_offset

                    if res[row][col] == 0:
                        res[row][col] = index
                        index += 1

        return res


x = Solution()
print(x.generateMatrix(0))
print(x.generateMatrix(1))
print(x.generateMatrix(2))
print(x.generateMatrix(3))
print(x.generateMatrix(4))
print(x.generateMatrix(5))
