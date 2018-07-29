class Solution:
    def largestRectangleArea(self, heights):
        stack, max_area = [], 0
        heights.append(0)
        for index in range(len(heights)):
            while stack and heights[stack[-1]] > heights[index]:
                height = stack.pop()
                max_area = max(max_area, heights[height] * (stack and index - stack[-1] - 1 or index))

            stack.append(index)

        return max_area

    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        left = [1]
        for index in range(1, len(heights)):
            if heights[index] > heights[index - 1]:
                left.append(1)
            else:
                j = index - 1
                while j >= 0 and heights[index] <= heights[j]:
                    j -= left[j]
 
                left.append(index - j)

        right = [0 for index in range(len(heights))]
        right[-1] = 1
        for index in range(len(heights) - 2, -1, -1):
            if heights[index + 1] < heights[index]:
                right[index] = 1
            else:
                j = index + 1
                while j < len(heights) and heights[index] <= heights[j]:
                    j += right[j]
                
                right[index] = j - index

        max_area = 0
        for index in range(len(heights)):
            max_area = max(max_area, heights[index] * (right[index] + left[index] - 1))

        return max_area


x = Solution()
print(x.largestRectangleArea([2,1,5,6,2,3]) == 10)
print(x.largestRectangleArea([1]) == 1)