def sort(items):
    merge_sort(items, 0, len(items))
    return items


def merge_sort(items, left, right):
    if left >= right - 1:
        return

    mid = left + ((right - left) >> 1)
    merge_sort(items, left, mid)
    merge_sort(items, mid, right)

    merge(items, left, mid, right)


def merge(items, left, mid, right):
    res = []
    i, j = left, mid
    while i < mid or j < right:
        if i < mid and j < right:
            if items[i] < items[j]:
                res.append(items[i])
                i += 1
            else:
                res.append(items[j])
                j += 1
        elif i < mid:
            res.append(items[i])
            i += 1
        else:
            res.append(items[j])
            j += 1

    for i in range(left, right):
        items[i] = res[i - left]
