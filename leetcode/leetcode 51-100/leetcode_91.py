class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        memo = {}
        def dfs(remaining_s):
            if remaining_s not in memo:
                if remaining_s.startswith('0'):
                    return 0

                if len(remaining_s) <= 1:
                    return 1

                count = dfs(remaining_s[1:])
                if remaining_s[:2] <= '26' and remaining_s[0] >= '1':
                    count += dfs(remaining_s[2:])

                memo[remaining_s] = count

            return memo[remaining_s]

        return dfs(s)


x = Solution()
print(x.numDecodings('12') == 2)
print(x.numDecodings('226') == 3)
print(x.numDecodings('20') == 1)
print(x.numDecodings('00') == 0)
print(x.numDecodings('01') == 0)

        