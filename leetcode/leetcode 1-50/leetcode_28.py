class Solution:

    def pre_handle(self, needle):
        res = [0]
        match_index = 0
        for word in needle[1:]:
            if match_index > 0 and needle[match_index] != word:
                match_index = res[match_index]

            if needle[match_index] == word:
                match_index += 1

            res.append(match_index)

        return res

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        kmp_lists = self.pre_handle(needle)

        needle_index = 0
        for index, word in enumerate(haystack):
            if word == needle[needle_index]:
                needle_index += 1
            else:
                while needle_index > 0 and word != needle[needle_index]:
                    needle_index = kmp_lists[needle_index - 1] + 1

            if needle_index == len(needle):
                return index - needle_index + 1

        return -1

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        try:
            return haystack.index(needle)
        except ValueError:
            return -1

    
x = Solution()
print (x.strStr2('hello', 'll'))
print (x.strStr2('aaaaa', 'bba'))
print (x.strStr2('a', 'a'))
print (x.strStr2('mississippi', 'issip'))