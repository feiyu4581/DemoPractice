import random

from quick_sort import sort


def search(items, target):
    left, right = 0, len(items) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if items[mid] == target:
            return mid
        elif items[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def search_first(items, target):
    """
    查找第一个值等于给定值的元素
    """
    left, right = 0, len(items) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if items[mid] == target:
            if mid == 0 or items[mid - 1] != target:
                return mid
            right = mid - 1
        elif items[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def search_first2(items, target):
    """
    查找第一个值等于给定值的元素
    """
    left, right = 0, len(items) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if items[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    if left < len(items) and items[left] == target:
        return left

    return -1


def search_last(items, target):
    """
    查找最后一个值等于给定值的元素
    """
    left, right = 0, len(items) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if items[mid] == target:
            if mid == len(items) - 1 or items[mid + 1] != target:
                return mid
            left = mid + 1
        elif items[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def search_first_bigger(items, target):
    """
    查找第一个大于等于给定值的元素
    """
    left, right = 0, len(items) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if items[mid] >= target:
            if mid == 0 and items[mid - 1] < target:
                return mid

            right = mid - 1
        else:
            left = mid + 1

    return -1


def search_last_less(items, target):
    """
    查找最后一个小于等于给定值的元素
    """
    left, right = 0, len(items) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if items[mid] <= target:
            if mid == len(items) - 1 or items[mid + 1] > target:
                return mid

            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    items = [random.randint(1, 10) for _ in range(20)]
    sort(items)

    print(f'Before: {items}')
    for _ in range(5):
        target = random.randint(1, 10)
        print(f'Target={target}, index={search_last_less(items, target)}, value={items[search_last_less(items, target)]}')
