class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        res, index, compare_s = '', 0, strs[0]
        while True:
            if index >= len(compare_s):
                return res

            for s in strs[1:]:
                if index >= len(s):
                    return res

                if compare_s[index] != s[index]:
                    return res

            res += compare_s[index]
            index += 1

    def longestCommonPrefix2(self, strs):
        if not strs:
            return ''

        strs.sort()
        left, right = strs[0], strs[-1]
        index, length = 0, min(len(left), len(right))
        while index < length:
            if left[index] != right[index]:
                break

            index += 1

        return left[:index]


x = Solution()

print(x.longestCommonPrefix2(["flower","flow","flight"]) == 'fl')
print(x.longestCommonPrefix2(["dog","racecar","car"]) == '')
print(x.longestCommonPrefix2(["a"]) == 'a')
