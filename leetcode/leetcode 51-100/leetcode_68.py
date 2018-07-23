import math


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, row, current_length = [], [], 0

        def justify(row, length, width, end=False):
            if len(row) == 1 or end:
                return ' '.join(row).ljust(width)

            remaining = width - length - len(row) + 1
            blanks = remaining // (len(row) - 1)
            extra_blanks = remaining % (len(row) - 1)

            res = ''
            for index, word in enumerate(row):
                res += word
                if remaining > 0:
                    blanks = min(blanks, remaining)
                    remaining -= blanks
                    res += ' ' * int(blanks)

                    if extra_blanks:
                        res += ' '
                        extra_blanks -= 1
                        remaining -= 1

                if index + 1 != len(row):
                    res += ' '

            return res

        for word in words:
            if current_length + len(word) + len(row) > maxWidth:
                res.append(justify(row, current_length, maxWidth))
                row = []
                current_length = 0

            current_length += len(word)
            row.append(word)

        res.append(justify(row, current_length, maxWidth, end=True))
        return res


x = Solution()

print(x.fullJustify(["so","fine","That","all","the"], 25) == [
    "so   fine  That  all  the"
])