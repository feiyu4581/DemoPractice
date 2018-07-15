class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        prev = len(nums) - 1
        for index in range(len(nums) - 2, -1, -1):
            if nums[index] < nums[prev]:
                compare_index = len(nums) - 1
                for compare_index in range(len(nums) - 1, index, -1):
                    if nums[compare_index] > nums[index]:
                        break

                nums[index], nums[compare_index] = nums[compare_index], nums[index]
                nums[index + 1:] = self.make_min(nums[index + 1:])

                break

            prev = index
        else:
            self.make_min(nums)

        return nums

    def make_min(self, nums):
        nums.sort()

        return nums


x = Solution()
print (x.nextPermutation([1, 2, 3]) == [1, 3, 2])
print (x.nextPermutation([3, 2, 1]) == [1, 2, 3])
print (x.nextPermutation([1, 1, 5]) == [1, 5, 1])
print (x.nextPermutation([1, 3, 2]) == [2, 1, 3])
print (x.nextPermutation([2, 3, 1]) == [3, 1, 2])
