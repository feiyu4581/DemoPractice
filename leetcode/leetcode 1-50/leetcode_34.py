class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        default = [-1, -1]
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                left, right = mid - 1, mid + 1
                while left >= 0 and nums[left] == target:
                    left -= 1

                while right < len(nums) and nums[right] == target:
                    right += 1

                return [left + 1, right - 1]

            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return default


x = Solution()
print (x.searchRange([5,7,7,8,8,10], 8))
print (x.searchRange([5,7,7,8,8,10], 6))