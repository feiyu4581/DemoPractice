class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, first = 0, True
        for index in range(len(s) - 1, -1, -1):
            if s[index] != ' ':
                first = False

            if s[index] == ' ' and not first:
                break

            if not first:
                res += 1

        return res
            


x = Solution()
print(x.lengthOfLastWord("Hello World") == 5)
print(x.lengthOfLastWord("a ") == 1)