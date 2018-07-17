class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        if len(num1) > len(num2):
            num1, num2 = num2, num1

        items, sequence = [], ''
        for dividor in reversed(num1):
            value, carry = sequence, 0
            for divide in reversed(num2):
                num = int(dividor) * int(divide) + carry
                carry = num // 10
                value = str(num % 10) + value

            if carry:
                value = str(carry) + value

            items.append(''.join(list(reversed(value))))
            sequence = '0' + sequence

        res, index, carry = '', 0, 0
        max_length = max(map(len, items))
        while index < max_length:
            num = carry
            for item in items:
                if index < len(item):
                    num += int(item[index])
            
            carry = num // 10
            res = str(num % 10) + res

            index += 1

        if carry:
            res = str(carry) + res

        return res


x = Solution()
print(x.multiply('2', '3') == '6')
print(x.multiply('123', '456') == '56088')
print(x.multiply('123456789', '987654321') == '121932631112635269') 
