class Solution:

    def trap(self, height):
        if len(height) is 0:
            return 0
        
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        
        watersum = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    watersum += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    watersum += rightmax - height[right]
                right -= 1
            
            
        return watersum

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        blocks, low_indexs, index = [], [0], 0
        for index in range(1, len(height)):     
            if height[index]:
                low_index = low_indexs.pop()
                if height[index] >= height[low_index]:
                    blocks.append((low_index, index))

                    while low_indexs and height[index] >= height[low_indexs[-1]]:
                        blocks.append((low_indexs.pop(), index))

                    low_indexs.append(index)
                else:
                    low_indexs.append(low_index)
                    low_indexs.append(index)

        if low_indexs:
            end = low_indexs[0] - 1
            low_indexs = [index]
            for index in range(index - 1, end, -1):
                if height[index]:
                    low_index = low_indexs.pop()
                    if height[index] >= height[low_index]:
                        blocks.append((index, low_index))

                        while low_indexs and height[index] >= height[low_indexs[-1]]:
                            blocks.append((index, low_indexs.pop()))

                        low_indexs.append(index)
                    else:
                        low_indexs.append(low_index)
                        low_indexs.append(index)

        blocks.sort(key=lambda block: (block[0], -block[1]))

        low_block = None
        res_blocks = []
        for block in blocks:
            if not low_block:
                low_block = block
                res_blocks.append(low_block)
            elif low_block[1] <= block[0]:
                res_blocks.append(block)
                low_block = block

        res = 0
        for low, high in res_blocks:
            value = (high - low - 1) * min(height[high], height[low])
            for index in range(low + 1, high):
                value -= height[index]

            if value > 0:
                res += value

        return res

x = Solution()
print (x.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)
print (x.trap([4,2,3]) == 1)
print (x.trap([9,8,2,6]) == 4)
        