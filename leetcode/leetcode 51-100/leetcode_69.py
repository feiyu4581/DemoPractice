class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        prev = 1
        start = (prev + x / prev) / 2

        while abs(start - prev) > 0.5:
            prev = start
            start = (prev + x / prev) / 2

        return int(start)

    
x = Solution()
# print(x.mySqrt(4) == 2)
print(x.mySqrt(8) == 2)
print(x.mySqrt(1) == 1)
print(x.mySqrt(3) == 1)
        