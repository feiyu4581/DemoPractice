class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.get_max_longest(s, 0, len(s) - 1, {})

    def get_max_longest(self, s, start, end, memorys):
        if (start, end) in memorys:
            return memorys[(start, end)]

        if start == end:
            return 1

        if end < start:
            return 0

        for index in range(start, end + 1):
            left_num = self.get_max_longest(s, start, index - 1, memorys)
            right_num = self.get_max_longest(s, index + 1, end, memorys)

            left_unique = ''
            for left in range(index, end + 1):
                if s[left] in left_unique:
                    break

                left_unique += s[left]

            right_unique = ''
            for right in range(index, start - 1, -1):
                if s[right] in right_unique:
                    break

                right_unique += s[right]

            max_unique = 0
            for index, left in enumerate(left_unique[1:]):
                if left in right_unique:
                    max_unique = len(right_unique) + index
                    break
            else:
                max_unique = len(right_unique) + len(left_unique) - 1

            for index, right in enumerate(right_unique[1:]):
                if right in left_unique:
                    max_unique = max(max_unique, len(left_unique) + index)
                    break
            else:
                max_unique = max(max_unique, len(right_unique) + len(left_unique) - 1)

            memorys[(start, end)] = max(left_num, right_num, max_unique)
            return memorys[(start, end)]


    def longest_sub_string(self, s):
        length = len(s)

        unique_s = set()
        ans, left, right = 0, 0, 0
        while (left < length and right < length):
            if s[right] not in unique_s:
                unique_s.add(s[right])
                right += 1
                ans = max(ans, right - left)
            else:
                unique_s.remove(s[left])
                left += 1

        return ans

    def longest_sub_string_2(self, s):
        length = len(s)

        ans, left, right = 0, 0, 0
        while (left < length and right < length):
            if s[right] not in s[left:right]:
                ans = max(ans, right - left + 1)
            else:
                left = max(left + s[left:right].index(s[right]) + 1, left + 1)

            right += 1

        return ans


x = Solution()
print (x.longest_sub_string_2('abcabcbb'))
print (x.longest_sub_string_2('bbbbb'))
print (x.longest_sub_string_2('pwwkew'))
print (x.longest_sub_string_2('bbtablud'))
print (x.longest_sub_string_2('ggububgvfk'))
