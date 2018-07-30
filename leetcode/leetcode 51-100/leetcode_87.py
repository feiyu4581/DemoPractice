class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}
        def is_scramble(s, target):
            if (s, target) not in memo:
                ans = False
                if len(s) != len(target) or str(sorted(s)) != str(sorted(target)):
                    ans = False
                elif s == target:
                    ans = True
                else:
                    for index in range(1, len(s)):
                        if is_scramble(s[:index], target[:index]) and is_scramble(s[index:], target[index:]):
                            ans = True
                            break

                        if is_scramble(s[:index], target[-index:]) and is_scramble(s[index:], target[:-index]):
                            ans = True
                            break
                
                memo[s, target] = ans

            return memo[s, target]

        return is_scramble(s1, s2)

x = Solution()
print(x.isScramble('great', 'rgeat') == True)
print(x.isScramble('abcde', 'caebd') == False)

        