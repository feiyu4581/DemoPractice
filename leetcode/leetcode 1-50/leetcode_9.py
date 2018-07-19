class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        nums = []
        current = x
        while current > 0:
            nums.append(current % 10)
            current = current // 10

        length = len(nums)
        for index in range(length // 2):
            if nums[index] != nums[length - index - 1]:
                return False

        return True

x = Solution()
print (x.isPalindrome(121))
print (x.isPalindrome(10))
print (x.isPalindrome(-121))
print (x.isPalindrome(12345677654321))