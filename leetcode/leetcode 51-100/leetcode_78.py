class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def sub(start, index):
            if index == 0:
                yield []
            else:
                for num in range(start, len(nums)):
                    if index == 1:
                        yield [nums[num]]
                    else:
                        for item in sub(num + 1, index - 1):
                            yield [nums[num]] + item

        return [
            item
            for index in range(len(nums) + 1)
            for item in sub(0, index)
        ]

            


x = Solution()
print(x.subsets([1,2,3]) == [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
])
        