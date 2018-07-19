class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        memory = {}
        res = []
        nums.sort(reverse=True)
        for index in range(len(nums)):
            two_sum = 0 - nums[index]
            if two_sum not in memory:
                two_sums = []
                for j in range(len(nums)):
                    start = 0
                    while start < len(nums):
                        try:
                            two_sum_index = nums.index(two_sum - nums[j], start)
                        except ValueError:
                            break
                        else:
                            if two_sum_index >= j:
                                break
                            two_sums.append([two_sum_index, j])
                            start = two_sum_index + 1
                memory[two_sum] = two_sums

            for result in memory[two_sum]:
                if index not in result:
                    three_sum = [nums[index], nums[result[0]], nums[result[1]]]
                    three_sum.sort()
                    if three_sum not in res:
                        res.append(three_sum)

        return res

    def threeSum2(self, nums):
        res = set()
        nums.sort()
        for index in range(len(nums)):
            left, right = index + 1, len(nums) - 1
            while (left < right):
                sums = nums[index] + nums[left] + nums[right]
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

    def threeSum3(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)

x = Solution()
print (x.threeSum3([-1, 0, 1, 2, -1, -4]))
print (x.threeSum3([0, 0, 0]))
print (x.threeSum3([-2,10,-14,11,5,-4,2,0,-10,-10,5,7,-11,10,-2,-5,2,12,-5,14,-11,-15,-5,12,0,13,8,7,10,6,-9,-15,1,14,11,-9,-13,-10,6,-8,-5,-11,6,-9,14,11,-7,-6,8,3,-7,5,-5,3,2,10,-6,-12,3,11,1,1,12,10,-8,0,8,-5,6,-8,-6,8,-12,-14,7,9,12,-15,-12,-2,-4,-4,-12,6,7,-3,-6,-14,-8,4,4,9,-10,-7,-4,-3,1,11,-1,-8,-12,9,7,-9,10,-1,-14,-1,-8,11,12,-5,-7]))
