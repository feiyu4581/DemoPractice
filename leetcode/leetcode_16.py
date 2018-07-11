class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 3:
            return sum(nums)

        nums.sort()
        max_sums = float('inf')
        for index in range(len(nums) - 2):
            left, right = index + 1, len(nums) - 1
            while left < right:
                sums = nums[index] + nums[left] + nums[right] - target
                if sums == 0:
                    return target
                elif sums > 0:
                    right -= 1
                else:
                    left += 1

                if abs(sums) < abs(max_sums):
                    max_sums = sums

        return target + max_sums


x = Solution()
print (x.threeSumClosest([-1,2,1,-4], 1))