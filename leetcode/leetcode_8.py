class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        negative = 1 
        limit = 2 ** 31 -1
        for index, w in enumerate(str.lstrip(' ')):
            if w in ('-', '+') and index == 0:
                negative = w == '-' and -1 or 1
                limit = w == '-' and 2 ** 31 or 2 ** 31 - 1
            elif w.isdigit():
                res = res * 10 + int(w)
                
                if res > limit:
                    return negative * limit
            else:
                return negative * res

        return negative * res

x = Solution()
print (x.myAtoi('42'))
print (x.myAtoi('   -42'))
print (x.myAtoi('4193 with words'))
print (x.myAtoi('words and 987'))
print (x.myAtoi('-91283472332'))
print (x.myAtoi('0-1'))
        