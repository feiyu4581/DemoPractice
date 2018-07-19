class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

x = Solution()
print (x.search([4,5,6,7,0,1,2], 0) == 4)
print (x.search([4,5,6,7,0,1,2], 3) == -1)
print (x.search([1, 3], 3) == 1)
print (x.search([3, 5, 1], 3) == 0)
