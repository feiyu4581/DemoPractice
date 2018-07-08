class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.get_longest_palindrome(s, 0, len(s) - 1)

    def get_longest_palindrome(self, s, start, stop):
        res = ''
        for index in range(start, stop + 1):
            middle = s[index]
            offset = 1
            while index - offset >= start and index + offset <= stop:
                if s[index - offset] == s[index + offset]:
                    middle = s[index - offset] + middle + s[index + offset]
                else:
                    break

                offset += 1

            if index + 1 <= stop and s[index] == s[index + 1]:
                even_middle = s[index] + s[index]
                offset = 1
                while index - offset >= start and index + 1 + offset <= stop:
                    if s[index - offset] == s[index + 1 + offset]:
                        even_middle = s[index - offset] + even_middle + s[index + 1 + offset]
                    else:
                        break

                    offset += 1

                middle = max(middle, even_middle, key=len)
        
            res = max(res, middle, key=len)

        return res

    def longestPublicString(self, s1, s2):
        return self.get_longest_public_string(s1, s2, len(s1) - 1, len(s2) - 1)

    def longestPalindrome_2(self, s):
        return self.get_longest_public_string(s, ''.join(reversed(s)), len(s) - 1, len(s) - 1)

    def get_longest_public_string(self, left, right, left_index, right_index):
        if left_index < 0 or right_index < 0:
            return ''

        if left[left_index] == right[right_index]:
            return self.get_longest_public_string(left, right, left_index - 1, right_index - 1) + left[left_index]
            
        return max(
            self.get_longest_public_string(left, right, left_index - 1, right_index),
            self.get_longest_public_string(left, right, left_index, right_index - 1),
            key=len
        )

    def longestPalindrome_3(self, s):
        s1 = '#' + '#'.join(s) + '#'
        n = len(s1)
        star = 0
        maxlen = 2
        for i in range(n):
            if i - maxlen >= 0 and s1[i-maxlen:i+1] == s1[i-maxlen:i+1][::-1]:
                star = i - maxlen
                maxlen += 2
        s2 = s1[star:star+maxlen-2]
        return ''.join(s2.split('#'))



x = Solution()
# print (x.longestPalindrome('babad'))
# print (x.longestPalindrome('cbbd'))
# print (x.longestPalindrome('aaaa'))

print(x.longestPalindrome_3('babad'))
print(x.longestPalindrome_3('cbbd'))
print(x.longestPalindrome_3('aaaa'))
print(x.longestPalindrome_3('abb'))
print(x.longestPalindrome_3('eabcb'))