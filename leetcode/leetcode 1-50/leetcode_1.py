class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            for j, num in enumerate(nums[index + 1:], start=index + 1):
                if num == target - nums[index]:
                    return [index, j]

        return []

    def dict_two_sum(self, nums, target):
        num_dict = {}
        for index in range(len(nums)):
            if target - nums[index] in num_dict:
                return [num_dict[target - nums[index]], index]

            num_dict[nums[index]] = index

        return []

x = Solution()
print (x.dict_two_sum([-1,-2,-3,-4,-5], -8))
print (x.two_sum([-1,-2,-3,-4,-5], -8))
print (x.dict_two_sum([2, 7, 11, 15], 9))
print (x.two_sum([2, 7, 11, 15], 9))