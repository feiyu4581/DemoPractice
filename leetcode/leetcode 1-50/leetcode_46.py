class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def match(remaining_nums):
            if not remaining_nums:
                yield []
            else:
                for index in range(len(remaining_nums)):
                    for remaining in match(remaining_nums[:index] + remaining_nums[index + 1:]):
                        yield [remaining_nums[index]] + remaining

        return list(item for item in match(nums))


x = Solution()
print (x.permute([1,2,3]) == [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
])