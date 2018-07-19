class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = ((dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0)) and 1 or -1
        dividend, divisor = abs(dividend), abs(divisor)

        if divisor > dividend:
            return 0

        limit = negative > 0 and 2 ** 31 - 1 or 2 ** 31
        remining = ''
        results = []
        for num in str(dividend):
            result, remining = self.subtraction(int(remining + num), divisor)
            results.append(result)

        if not results:
            return 0

        return min(int(''.join(results)), limit) * negative

    def subtraction(self, divident, divisor):
        res = 0
        while divident >= divisor:
            divident -= divisor
            res += 1

        return str(res), str(divident)


x = Solution()
# print(x.divide(10, 3))
# print(x.divide(7, -3))
print(x.divide(-1, 1))