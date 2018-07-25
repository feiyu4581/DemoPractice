class Solution:
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        before_num, before_count = None, 0
        for index in range(len(nums)):
            if before_num is None:
                before_num = nums[index]
                before_count = 1
            elif nums[index] == before_num:
                if before_count == 2:
                    nums[index] = '*'
                else:
                    before_count += 1
            else:
                before_num = nums[index]
                before_count = 1

        low = 0
        for index in range(len(nums)):
            if nums[index] != '*':
                if index != low:
                    nums[index], nums[low] = nums[low], nums[index]
                low += 1

        return low

    
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        if len(nums) <= 2:
            return len(nums)

        low = 0
        for index in range(2, len(nums)):
            if nums[low] != nums[index]:
                nums[low + 2] = nums[index]
                low += 1

        return low + 2


x = Solution()
print(x.removeDuplicates([0,0,0,0,0]) == 2)
print(x.removeDuplicates([1,1,1,2,2,3]) == 5)
print(x.removeDuplicates([0,0,1,1,1,1,2,3,3]) == 7)
        