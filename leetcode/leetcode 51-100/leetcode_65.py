class Solution:
    def isNumber(self, s):
        s = s.strip()
        if not s:
            return False

        def get_num(nums, digit=False):
            before_nums = ''
            for index, num in enumerate(nums):
                if num in '0123456789':
                    before_nums += num
                elif num in '-+' and index == 0:
                    continue
                elif num == '.':
                    if digit:
                        return False

                    digit = True
                else:
                    return False

            return bool(before_nums)

        if 'e' in s:
            index = s.index('e')
            return get_num(s[0:index]) and get_num(s[index + 1:], True)
        else:
            return get_num(s)


x = Solution()
print(x.isNumber("0") == True)
print(x.isNumber(" 0.1 ") == True)
print(x.isNumber("abc") == False)
print(x.isNumber("1 a") == False)
print(x.isNumber("2e10") == True)
print(x.isNumber("e") == False)
print(x.isNumber(".1") == True)
print(x.isNumber(".") == False)
print(x.isNumber(".e1") == False)
print(x.isNumber("3.") == True)
print(x.isNumber("-3.") == True)
print(x.isNumber("+.8") == True)
print(x.isNumber(" -.") == False)
print(x.isNumber("46.e3") == True)
print(x.isNumber("0e") == False)
print(x.isNumber("1e.") == False)
print(x.isNumber("6e6.5") == False)
        