class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area, left, right = 0, 0, len(height) - 1

        while (left < right):
            max_area = max(max_area, min(height[right], height[left]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

x = Solution()
print (x.maxArea([1, 2, 3, 4]))
print (x.maxArea([1, 1]))
        