class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()
        for index in range(len(nums)):
            for three_sum in self.threeSum(nums[index + 1:], target - nums[index]):
                sums = tuple([nums[index]] + three_sum)
                if sums not in res:
                    res.add(sums)

        return map(list, list(res))

    def threeSum(self, nums, target):
        res = set()
        for index in range(len(nums) - 2):
            left, right = index + 1, len(nums) - 1
            while (left < right):
                sums = nums[index] + nums[left] + nums[right] - target
                if sums == 0:
                    sum_array = (nums[index], nums[left], nums[right])
                    res.add(sum_array)

                    left += 1
                    right -= 1
                elif sums > 0:
                    right -= 1
                else:
                    left += 1

        return map(list, list(res))


    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def NSum(nums, target, N):
            n = len(nums)
            if n < N or nums[0] * N > target or nums[-1] * N < target:
                return []
            res = []
            if N == 2:
                l,r = 0, n-1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append([nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:l += 1
                        while l < r and nums[r] == nums[r+1]:r -= 1
                return res
            else:
                for i in range(n-N+1):
                    if i == 0 or nums[i] != nums[i-1]:
                        for pre in NSum(nums[i+1:],target-nums[i],N-1):
                            res.append([nums[i]] + pre)  
                return res
            
        return NSum(sorted(nums),target,4)
            
x = Solution()
# print (x.fourSum([1, 0, -1, 0, -2, 2], 0))
print (x.fourSum2([-1,-5,-5,-3,2,5,0,4], -7))