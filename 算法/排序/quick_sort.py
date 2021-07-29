def sort(items):
    # quick_sort(items, 0, len(items))
    quick_sort_with_stack(items, 0, len(items))
    return items


def quick_sort(items, left, right):
    """
    使用递归方式实行快速排序
    """
    if left >= right - 1:
        return

    # index = partition(items, left, right)
    index = partition_with_double_pointer(items, left, right)
    quick_sort(items, left, index)
    quick_sort(items, index + 1, right)


def quick_sort_with_stack(items, left, right):
    """
    使用栈的方式实现快速排序
    """
    stack = [(left, right)]
    while stack:
        i, j = stack.pop()

        if i >= j - 1:
            continue

        index = partition_with_double_pointer(items, i, j)
        stack.append((i, index))
        stack.append((index + 1, j))


def choose_k_nums(items, k):
    # 第一位等价于第 0 个数据
    return items[quick_choose_k_nums(items, 0, len(items), k - 1)]


def quick_choose_k_nums(items, left, right, k):
    """
    使用快速排序高效的查找第 k 个排序的数据
    """
    if k < left or k >= right:
        return -1

    index = partition_with_double_pointer(items, left, right)
    if index == k:
        return index
    elif index > k:
        return quick_choose_k_nums(items, left, index, k)
    else:
        return quick_choose_k_nums(items, index + 1, right, k)


def partition(items, left, right):
    # 维护一个 items[left:index] 的位置，这个位置里面的数据都是小于比较值的数据
    choose_mid(items, left, right)
    index, p, comp = left, right - 2, items[right - 1]
    while p >= index:
        if items[p] < comp:
            items[index], items[p] = items[p], items[index]
            index += 1
        else:
            p -= 1

    items[index], items[right - 1] = items[right - 1], items[index]
    return index


def partition_with_double_pointer(items, left, right):
    # 使用双指针的方式来实现快速排序
    choose_mid(items, left, right)
    i, j, current = left, right - 2, items[right - 1]
    while i <= j:
        if items[i] > current > items[j]:
            items[i], items[j] = items[j], items[i]
            i += 1
            j -= 1

        if items[i] <= current:
            i += 1

        if items[j] >= current:
            j -= 1

    items[i], items[right - 1] = items[right - 1], items[i]
    return i


def choose_mid(items, left, right):
    # 取左边、右边、中间三者的中间值放到最右边的位置上
    if left + 1 >= right - 1:
        return

    mid = left + ((right - left) >> 1)
    if items[left] > items[right - 1]:
        items[right - 1], items[left] = items[left], items[right - 1]

    if items[mid] < items[left] < items[right - 1]:
        items[left], items[right - 1] = items[right - 1], items[left]
    elif items[left] < items[mid] < items[right - 1]:
        items[right - 1], items[mid] = items[mid], items[right - 1]
