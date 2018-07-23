class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        index = len(digits) - 1
        digits[index] += 1
        while index >= 0:
            if digits[index] == 10:
                digits[index] = 0
                carry = 1
                index -= 1
            elif carry > 0:
                digits[index] += carry
                carry = 0
            else:
                break

        if carry > 0:
            digits = [1] + digits

        return digits

x = Solution()
# print(x.plusOne([1,2,3]) == [1,2,4])
# print(x.plusOne([4,3,2,1]) == [4,3,2,2])
# print(x.plusOne([9]) == [1, 0])
print(x.plusOne([8, 9, 9, 9]) == [9, 0, 0, 0])
        