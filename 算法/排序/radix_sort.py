from counting_sort import sort as counting_sort


def sort(items, nums=10):
    for i in range(nums - 1, -1, -1):
        items = counting_sort(items, key=lambda item: int(item[i]))

    return items
