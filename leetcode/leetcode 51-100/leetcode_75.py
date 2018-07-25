class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = {0: 0, 1: 0, 2: 0}
        for num in nums:
            counter[num] += 1

        index = 0
        for num, count in counter.items():
            for _ in range(count):
                nums[index] = num
                index += 1

        return nums

    def sortColors2(self, nums):
        low, high, index = 0, len(nums) - 1, 0
        while index <= high:
            if nums[index] == 0:
                nums[index], nums[low] = nums[low], nums[index]
                low += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[high] = nums[high], nums[index]
                high -= 1
            else:
                index += 1

        return nums

x = Solution()
print(x.sortColors2([2,0,2,1,1,0]) == [0,0,1,1,2,2])
        