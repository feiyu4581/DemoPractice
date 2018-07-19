class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return []

        def queens(row, columns, left_slashs, slashs):
            if row >= n:
                return []

            skips = columns | slashs | left_slashs
            res = []
            for column in range(n):
                if column not in skips:
                    current = ['.'] * n
                    current[column] = 'Q'
                    current = [''.join(current)]

                    new_slashs = {column + 1, }
                    for slash in slashs:
                        new_slashs.add(slash + 1)

                    new_left_slashs = {column - 1, }
                    for slash in left_slashs:
                        new_left_slashs.add(slash - 1)

                    for ans in queens(row + 1, columns | {column, }, new_left_slashs, new_slashs):
                        if len(ans) == n - row - 1:
                            res.append(current + ans)

                    if n == row + 1:
                        res.append(current)

            return res

        return queens(0, set(), set(), set())


x = Solution()
print (x.solveNQueens(4) == [
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
])