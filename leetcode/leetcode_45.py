class Solution:
    def jump(self, nums):
        # 维护一个滑动窗口，每次找到当前窗口能覆盖的最大范围，下一次循环滑动到上个窗口的结束到最大范围，开始找下一个最大范围，直到序列结束
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

    def jump2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        memo = {}
        def match(low, high):
            nonlocal memo, nums
            if (low, high) not in memo:
                ans = float('inf')
                if low >= high:
                    ans = 0
                elif nums[low] >= high - low:
                    ans = 1
                else:
                    for index in range(nums[low], 0, -1):
                        remaining = match(low + index, high)
                        if remaining == 1:
                            ans = 2
                            break
                        else:
                            ans = min(ans, remaining + 1)
                
                memo[(low, high)] = ans
            return memo[(low, high)]

        return match(0, len(nums) - 1)
    

x = Solution()
print(x.jump([2,3,1,1,4]) == 2)
