import collections


class Solution:
    def get_normal(self, s):
        left_pot = s.find('.')
        left_star = s.find('*') - 1

        right_pot = s.rfind('.')
        right_star = s.rfind('*')
    
        left = min(left_pot == -1 and len(s) or left_pot, left_star == -2 and len(s) or left_star)
        right = max(right_pot != -1 and right_pot or 0, right_star != -1 and right_star or 0)
        return s[0:left], s[right + 1:]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_length, p_length = len(s), len(p)
        if '*' not in p and p_length != s_length:
            return False

        if p_length == 0:
            return s_length == p_length

        starts_normal, ends_normal = self.get_normal(p)
        if not s.startswith(starts_normal) or not s.endswith(ends_normal):
            return False

        if (p_length == 1 or p[1] != '*'):
            return bool(s_length) and (p[0] == '.' or p[0] == s[0]) and self.isMatch(s[1:], p[1:])
        else:
            s_index = 0
            while s_index < s_length and (p[0] == '.' or s[s_index] == p[0]):
                if self.isMatch(s[s_index + 1:], p[2:]):
                    return True

                s_index += 1

        return self.isMatch(s[0:], p[2:])

    def isMatch2(self, s, p):
        if not p: return not s
        memo = {}
        def match(i, j):
            if (i,j) not in memo:
                if j == len(p): ans = i == len(s)
                else:
                    firstmatch = len(s) > i and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = match(i, j+2) or firstmatch and match(i+1, j)
                    else:
                        ans = firstmatch and match(i+1, j+1)
                memo[i, j] = ans
            return memo[i,j]
        
        return match(0, 0)

    def isMatch3(self, s, p):
        if not p:
            return not s

        memo = {}
        def match(i, j):
            if (i, j) not in memo:
                ans = False
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = match(i, j + 2) or (first_match and match(i + 1, j))
                    else:
                        ans = first_match and match(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return match(0, 0)


x = Solution()
print (x.isMatch3('aa', 'a'))
print (x.isMatch3('aa', 'a*'))
print (x.isMatch3('ab', '.*'))
print (x.isMatch3('aab', 'c*a*b'))
print (x.isMatch3('mississippi', 'mis*is*p*.'))
print (x.isMatch3('ab', '.*c'))
print (x.isMatch3('aaa', 'aaaa'))
print (x.isMatch3('aaa', 'a*a'))
print (x.isMatch3('a', 'ab*'))
print (x.isMatch3('bbbba', '.*a*a'))

print (x.isMatch3('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c'))