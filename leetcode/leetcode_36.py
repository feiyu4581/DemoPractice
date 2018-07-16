class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = {}
        for row in range(9):
            for column in range(9):
                item = board[row][column]
                if item and item != '.':
                    res.setdefault(item, [])
                    res[item].append((row, column))

        for locations in res.values():
            rows, columns, blocks = set(), set(), set()
            for location in locations:
                row, column, block = location[0], location[1], (location[0] // 3, location[1] // 3)

                if row in rows or column in columns or block in blocks:
                    return False

                rows.add(row)
                columns.add(column)
                blocks.add(block)

        return True


x = Solution()
print (x.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

print (x.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))