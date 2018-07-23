class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans, index, carry = '', 1, 0
        while index <= len(a) or index <= len(b):
            left = index <= len(a) and int(a[-index]) or 0
            right = index <= len(b) and int(b[-index]) or 0

            value = left + right + carry
            carry = 0
            if value > 1:
                value -= 2
                carry = 1

            ans = str(value) + ans
            index += 1

        if carry == 1:
            ans = '1' + ans

        return ans
            

x = Solution()
print(x.addBinary('11', '1') == '100')
print(x.addBinary('1010', '1011') == '10101')
print(x.addBinary('1111', '1111') == '11110')

        