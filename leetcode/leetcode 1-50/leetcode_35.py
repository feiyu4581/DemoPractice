class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low

x = Solution()
print(x.searchInsert([1,3,5,6], 5) == 2)
print(x.searchInsert([1,3,5,6], 2) == 1)
print(x.searchInsert([1,3,5,6], 7) == 4)
print(x.searchInsert([1,3,5,6], 0) == 0)
