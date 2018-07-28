class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []

        def match(start, nums):
            for num in range(start, n + 1):
                if nums == 1:
                    yield [num]
                else:
                    for item in match(num + 1, nums - 1):
                        yield [num] + item

        return [item for item in match(1, k)]


x = Solution()
print(x.combine(4, 2) == [
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
])
        