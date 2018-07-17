class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(len(nums)):
            if nums[index] < 0:
                nums[index] = 0

        for num in nums:
            num = abs(num)
            if num and num <= len(nums):
                nums[num - 1] = -abs(nums[num - 1]) or -num

        res = 0
        while res < len(nums) and nums[res] < 0:
            res += 1

        return res + 1
    
x = Solution()
print (x.firstMissingPositive([1,2,0]) == 3)
print (x.firstMissingPositive([3,4,-1,1]) == 2)
print (x.firstMissingPositive([7,8,9,11,12]) == 1)
print (x.firstMissingPositive([2, 2]) == 1)