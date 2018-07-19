class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman_convert = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1),
        ]

        res = ''
        for convert in roman_convert:
            if num >= convert[1]:
                nums = num // convert[1]
                num = num % convert[1]

                res += convert[0] * nums

        return res

x = Solution()
print (x.intToRoman(3) == 'III')
print (x.intToRoman(4) == 'IV')
print (x.intToRoman(9) == 'IX')
print (x.intToRoman(58) == 'LVIII')
print (x.intToRoman(1994) == 'MCMXCIV')