class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit = x > 0 and 2 ** 31 - 1 or 2 ** 31
        negative = x < 0 and -1 or 1

        res = int(''.join(reversed(str(abs(x)))))
        if res > limit:
            return 0

        return negative * res


x = Solution()
print (x.reverse(123))
print (x.reverse(-123))