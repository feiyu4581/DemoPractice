class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return p == s

        memo = {}
        def match(i, j):
            nonlocal memo
            if (i, j) not in memo:
                ans = False
                if j == len(p):
                    ans = i == len(s)
                elif i < len(s) and p[j] in {'?', s[i]}:
                    ans = match(i + 1, j + 1)
                elif p[j] == '*':
                    ans = match(i, j + 1) or (i < len(s) and match(i + 1, j))

                memo[(i, j)] = ans
                
            return memo[(i, j)]

        return match(0, 0)

x = Solution()
print (x.isMatch('aa', 'a') == False)
print (x.isMatch('aa', '*') == True)
print (x.isMatch('cb', '?a') == False)
print (x.isMatch('adceb', '*a*b') == True)
print (x.isMatch('acdcb', 'a*c?b') == False)