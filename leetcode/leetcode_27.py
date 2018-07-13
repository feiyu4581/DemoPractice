class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        location = 0
        for index, num in enumerate(nums, start=0):
            if num != val:
                if location != index:
                    nums[location] = num

                location += 1

        return location

x = Solution()

nums = [3,2,2,3]
index = x.removeElement(nums, 3)
print(nums[:index])

nums = [0,1,2,2,3,0,4,2]
index = x.removeElement(nums, 2)
print(nums[:index])

