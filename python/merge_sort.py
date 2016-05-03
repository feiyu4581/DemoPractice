
import random
import math


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


def merge_sort(array):
    if len(array) <= 1:
        return array

    center_index = int(math.ceil(len(array) / 2))
    left_array = merge_sort(array[0:center_index])
    right_array = merge_sort(array[center_index:])

    return merge(left_array, right_array)


if __name__ == '__main__':
    shuffle_array = [random.randint(1, 100) for i in range(10)]
    print 'shuffle_array: ', shuffle_array
    sorting_array = merge_sort(shuffle_array)

    print 'sorting: ', sorting_array
