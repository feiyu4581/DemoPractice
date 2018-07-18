class Solution:
    def permuteUnique(self, nums):
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

        res = set()
        for item in match(nums):
            res.add(tuple(item))

        return list(res)

    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def match(remaining_nums):
            if not remaining_nums:
                yield []
            else:
                for index in range(len(remaining_nums)):
                    if index > 0 and remaining_nums[index] == remaining_nums[index - 1]:
                        continue

                    for remaining in match(remaining_nums[:index] + remaining_nums[index + 1:]):
                        yield [remaining_nums[index]] + remaining

        nums.sort()
        return list(item for item in match(nums))


x = Solution()
print (x.permuteUnique2([1,1,2]) == [
  [1,1,2],
  [1,2,1],
  [2,1,1]
])