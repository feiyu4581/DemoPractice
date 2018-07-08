class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_length, p_length = len(s), len(p)
        if p_length == 0:
            return s_length == p_length

        if (p_length == 1 or p[1] != '*'):
            return bool(s_length) and (p[0] == '.' or p[0] == s[0]) and self.isMatch(s[1:], p[1:])
        else:
            s_index = 0
            while s_index < s_length and (p[0] == '.' or s[s_index] == p[0]):
                if self.isMatch(s[s_index + 1:], p[2:]):
                    return True

                s_index += 1

            return self.isMatch(s[0:], p[2:])

x = Solution()
print (x.isMatch('aa', 'a'))
print (x.isMatch('aa', 'a*'))
print (x.isMatch('ab', '.*'))
print (x.isMatch('aab', 'c*a*b'))
print (x.isMatch('mississippi', 'mis*is*p*.'))
print (x.isMatch('ab', '.*c'))
print (x.isMatch('aaa', 'aaaa'))
print (x.isMatch('aaa', 'a*a'))
print (x.isMatch('a', 'ab*'))
print (x.isMatch('bbbba', '.*a*a'))