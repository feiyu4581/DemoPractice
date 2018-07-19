class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True

        start, end = 0, nums[0] + 1
        while True:
            if end >= len(nums):
                return True

            max_end = max(index + nums[index] for index in range(start, end))
            if max_end < end:
                return False

            start, end = end, max_end + 1

    def canJump2(self, nums):
        index = len(nums) - 1
        for col in range(len(nums) - 2, -1, -1):
            if col + nums[col] >= index:
                index = col

        return index == 0

        
x = Solution()
print(x.canJump2([2,3,1,1,4]) == True)
print(x.canJump2([3,2,1,0,4]) == False)
print(x.canJump2([1, 2, 3]) == True)
print(x.canJump2([2, 0]) == True)
print(x.canJump2([1, 1, 1, 0]) == True)