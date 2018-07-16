class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        stack = []
        exists = {
            num: {
                'rows': set(),
                'columns': set(),
                'blocks': set()
            }
            for num in '123456789'
        }
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num != '.':
                    exists[num]['rows'].add(row)
                    exists[num]['columns'].add(column)
                    exists[num]['blocks'].add((row // 3, column // 3))
                else:
                    stack.append((row, column))

        def func(prev_num=None, prev_row=None, prev_col=None):
            nonlocal exists, board, stack
            if not stack:
                return

            row, col = stack.pop()
            for num in '123456789':
                rows, cols, blocks = exists[num]['rows'], exists[num]['columns'], exists[num]['blocks']
                if row not in rows and col not in cols and (row // 3, col // 3) not in blocks:
                    rows.add(row)
                    cols.add(col)
                    blocks.add((row // 3, col // 3))
                    board[row][col] = num
                    func(num, row, col)

                    if not stack:
                        return

            stack.append((row, col))
            if prev_num:
                exists[prev_num]['rows'].remove(prev_row)
                exists[prev_num]['columns'].remove(prev_col)
                exists[prev_num]['blocks'].remove((prev_row // 3, prev_col // 3))
                board[prev_row][prev_col] = '.'

        func()
        return board

x = Solution()
for rows in x.solveSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]):
    print (', '.join(rows))

