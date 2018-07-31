class Solution:
    def subsetsWithDup2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, temps = set(), []
        def dfs(index):
            nonlocal res, temps
            tuple_temp = tuple(sorted(temps))
            if tuple_temp not in res:
                res.add(tuple_temp)
            for num in range(index, len(nums)):
                temps.append(nums[num])
                dfs(num + 1)
                temps.pop()

        dfs(0)

        return list(map(list, res))

    def subsetsWithDup(self, nums):
        nums.sort()
        res, length = set(), len(nums)
        for index in range(2 ** length):
            temp = []

            bin_index = bin(index)[2:].rjust(length, '0')
            for num, char in enumerate(bin_index):
                if char == '1':
                    temp.append(nums[num])

            tuple_temp = tuple(temp)
            if tuple_temp not in res:
                res.add(tuple_temp)

        return list(map(list, res))
    


x = Solution()
print(x.subsetsWithDup([1,2,2]))
print(x.subsetsWithDup([4, 4, 4, 1, 4]))