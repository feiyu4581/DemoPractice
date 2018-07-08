class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)

        res = ''

        if numRows == 1:
            return s

        for row in range(numRows):
            start = row
            while start < length:
                res += s[start]
                if row != 0 and row != numRows - 1 and start + 2 * (numRows - row - 1) < length:
                    res += s[start + 2 * (numRows - row - 1)]

                start += 2 * numRows - 2

        return res


x = Solution()
print (x.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
print (x.convert('A', 1) == 'A')