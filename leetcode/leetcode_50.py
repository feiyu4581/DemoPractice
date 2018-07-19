class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not x:
            return 0

        memo = {}
        def multi(num):
            nonlocal memo, x
            if num not in memo:
                if num == 0:
                    ans = 1
                elif num == 1:
                    ans = x
                else:
                    mid = num // 2
                    ans = multi(mid) * multi(num - mid)

                memo[num] = ans

            return memo[num]

        if n < 0:
            x = 1.0 / x
            n = -n

        return multi(n)
    
x = Solution()
print (x.myPow(2.00000, 10) == 1024.00000)
print (x.myPow(2.10000, 3) == 9.26100)
print (x.myPow(2.00000, -2) == 0.25000)
