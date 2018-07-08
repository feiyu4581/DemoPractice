class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        length_1, length_2 = len(nums1), len(nums2)
        if length_1 > length_2:
            return self.findMedianSortedArrays(nums2, nums1)

        inf, un_inf = float('inf'), float('-inf')
        min_index, max_index = 0, 2 * length_1
        while min_index <= max_index:
            i = int((min_index + max_index) / 2)
            j = length_1 + length_2 - i

            left_1 = i == 0 and un_inf or nums1[int((i - 1) / 2)]
            right_1 = i == 2 * length_1 and inf or nums1[int((i / 2))]

            left_2 = j == 0 and un_inf or nums2[int((j - 1) / 2)]
            right_2 = j == 2 * length_2 and inf or nums2[int((j / 2))]

            if left_1 > right_2:
                max_index = i - 1
            elif left_2 > right_1:
                min_index = i + 1
            else:
                break

        return (max(left_1, left_2) + min(right_1, right_2)) / 2
        
x = Solution()
print(x.findMedianSortedArrays([5], [1, 2, 3, 4]))
print(x.findMedianSortedArrays([1], []))
print(x.findMedianSortedArrays([6], [1,2,3,4,5,7,8,9,10]))