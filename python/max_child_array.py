
import random
import math

# 假定要寻找子数组A[low, high]的最大子数组。使用分治技术意味着我们要将子数组划分为两个规模尽量相等的子数组。
# 也就是说，找到子数组的中央位置，比如mid，然后考虑求解两个子数组A[low, mid]和A[mid + , high]，此时，
# A[low, high]的任何连续子数组A[i...j]所处的位置必然是以下三种情况
# 1. 完全位于子数组A[low, mid]中，因此 low <= i <= j <= mid.
# 2. 完全位于子数组A[mid + 1, low]中，因此 mid <= i <= j <= high.
# 3. 跨越了中点，因此 low <= i <= mid <= j <= high.
# 因此，存在一个最大子数组必定存在于上述三个情况中的一个
# 所以，分别求出三个情况的解，比较得到最大值即可


def merge(left, right):
    res = []
    left_length, right_length = 0, 0

    while left_length < len(left) and right_length < len(right):
        if left[left_length] < right[right_length]:
            res.append(left[left_length])
            left_length += 1
        else:
            res.append(right[right_length])
            right_length += 1

    last_array = len(left) >= left_length and right[right_length:] or left[left_length:]
    res.extend(last_array)

    return res


def find_mid_sum(array, low, high, mid):
    left_sum, right_sum = -101, -101
    left_offset, right_offset = 0, 0

    all_sum = 0
    for left in range(mid, low - 1, -1):
        all_sum += array[left]
        if all_sum > left_sum:
            left_sum = all_sum
            left_offset = left

    all_sum = 0
    for right in range(mid + 1, high + 1):
        all_sum += array[right]
        if all_sum > right_sum:
            right_sum = all_sum
            right_offset = right

    return (left_offset, right_offset, left_sum + right_sum)


def max_child_array(array, low, high):
    if low == high:
        return (low, high, array[0])

    # 获取中间值，作为分解点
    mid = int(math.floor((high + low) / 2))

    left_sum = max_child_array(array, low, mid)
    right_sum = max_child_array(array, mid + 1, high)

    mid_sum = find_mid_sum(array, low, high, mid)

    return max([left_sum, right_sum, mid_sum], key=lambda amount: amount[2])


if __name__ == '__main__':
    array = [random.randint(-100, 100) for i in range(10)]
    print 'origin array: ', array
    child_array = max_child_array(array, 0, len(array) - 1)

    print 'child array: ', child_array
