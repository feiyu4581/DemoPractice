class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        last, location = nums[0], 1
        for index, num in enumerate(nums[1:], start=1):
            if num != last:
                if location != index:
                    nums[location] = num

                last = num
                location += 1

        return location

x = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
index = x.removeDuplicates(nums)
print(nums[:index])

nums = [1, 2]
index = x.removeDuplicates(nums)
print(nums[:index])

