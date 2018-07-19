class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return []

        def queens(row, columns, left_slashs, slashs):
            if row >= n:
                return 0

            skips = columns | slashs | left_slashs
            res = 0
            for column in range(n):
                if column not in skips:
                    new_slashs = {column + 1, }
                    for slash in slashs:
                        new_slashs.add(slash + 1)

                    new_left_slashs = {column - 1, }
                    for slash in left_slashs:
                        new_left_slashs.add(slash - 1)

                    res += queens(row + 1, columns | {column, }, new_left_slashs, new_slashs)

                    if n == row + 1:
                        res += 1

            return res

        return queens(0, set(), set(), set())


x = Solution()
print(x.totalNQueens(4) == 2)