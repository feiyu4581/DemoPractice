class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        res, max_sum = nums[0], 0
        for num in nums:
            if max_sum < 0:
                max_sum = 0

            max_sum += num
            res = max(res, max_sum)

        return res

    def maxSubArray2(self, nums):
        if not nums:
            return 0

        dp = [nums[0]]
        ans = dp[0]
        for index in range(1, len(nums)):
            dp.append(max(dp[index - 1] + nums[index], nums[index]))
            ans = max(dp[index], ans)

        return ans


x = Solution()
print(x.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(x.maxSubArray2([-2,1]) == 1)
print(x.maxSubArray2([-1,1,2,1]) == 4)
print(x.maxSubArray2([-2, -1]) == -1)
print(x.maxSubArray2([0]) == 0)
print(x.maxSubArray2([1, 2]) == 3)
