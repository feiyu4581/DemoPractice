class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_digits_maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []

        def combination(s):
            if s:
                for digit in letter_digits_maps[s[0]]:
                    for combination_digit in combination(s[1:]):
                        yield digit + combination_digit
            else:
                yield ''

        return list(combination(digits))
                    


        


x = Solution()
print (x.letterCombinations('23'))
print (x.letterCombinations(''))
