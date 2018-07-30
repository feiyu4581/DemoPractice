class Solution:
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        if n > 0:
            nums1[:m] = nums2[:n]

        return nums1
        

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        start = m + n - 1
        for index in range(m - 1, -1, -1):
            nums1[start] = nums1[index]
            start -= 1

        index, left_index, right_index = 0, n, 0
        while left_index < m + n or right_index < n:
            if right_index >= n or (left_index < m + n and nums1[left_index] < nums2[right_index]):
                nums1[index] = nums1[left_index]
                left_index += 1
            else:
                nums1[index] = nums2[right_index]
                right_index += 1

            index += 1

        return nums1


x = Solution()
print(x.merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6])