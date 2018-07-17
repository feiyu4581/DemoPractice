class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_map = {}
        def compute_match(index):
            nonlocal nums_map
            if index not in nums_map:
                index_maps = []
                for num in candidates:
                    if num == index:
                        index_maps.append([index])
                    elif num < index:
                        for remaining in compute_match(index - num):
                            index_maps.append([num] + remaining)

                nums_map[index] = index_maps

            return nums_map[index]

        compute_match(target)
        res = []
        for num in nums_map[target]:
            num.sort()
            if num not in res:
                res.append(num)

        return res
x = Solution()
print (x.combinationSum([2,3,6,7], 7))
print (x.combinationSum([2,3,5], 8))
