class Solution:
    def combinationSum2(self, candidates, target):
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
                for i, num in enumerate(candidates):
                    if num == index:
                        index_maps.append({i, })
                    elif num < index:
                        for remaining in compute_match(index - num):
                            if i not in remaining:
                                index_maps.append(remaining.union({i, }))

                nums_map[index] = index_maps

            return nums_map[index]

        compute_match(target)
        res = []
        for num in nums_map[target]:
            num = list(sorted((map(lambda item: candidates[item], num))))
            if num not in res:
                res.append(num)

        return res

x = Solution()
print (x.combinationSum2([10,1,2,7,6,1,5], 8))
print (x.combinationSum2([2,5,2,1,2], 5))
print (x.combinationSum2([29,19,14,33,11,5,9,23,23,33,12,9,25,25,12,21,14,11,20,30,17,19,5,6,6,5,5,11,12,25,31,28,31,33,27,7,33,31,17,13,21,24,17,12,6,16,20,16,22,5], 28))
