class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_convert = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }

        index, length = 0, len(s)
        res = 0
        while index < length:
            if index + 1 < length and s[index:index + 2] in roman_convert:
                res += roman_convert[s[index:index + 2]]
                index += 2
            else:
                res += roman_convert[s[index]]
                index += 1

        return res


x = Solution()
print (x.romanToInt('III') == 3)
print (x.romanToInt('IV') == 4)
print (x.romanToInt('IX') == 9)
print (x.romanToInt('LVIII') == 58)
print (x.romanToInt('MCMXCIV') == 1994)