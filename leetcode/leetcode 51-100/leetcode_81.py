class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right :
            mid = (left+right) // 2
            if nums[mid] == target : return True
            if nums[mid] == nums[left] : left += 1
            elif nums[mid] > nums[left] :
                if nums[mid] > target and nums[left] <= target :
                    right = mid - 1
                else : left = mid + 1
            else :
                if nums[mid] < target and nums[right] >= target :
                    left = mid + 1
                else : right = mid - 1
        return False


    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True

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

        return False


x = Solution()
print(x.search([2,5,6,0,0,1,2], 0) == True)
print(x.search([2,5,6,0,0,1,2], 3) == False)
print(x.search([1,3,1,1,1], 3) == True)
print(x.search([1,1,3,1], 3) == True)
print(x.search([3, 1], 1) == True)