from quick_sort import sort as quick_sort


def sort(items, nums=10):
    max_data = max(max(items) + 1, nums)

    buckets = [[] for _ in range(nums)]
    for item in items:
        position = int((float(item) / max_data) * nums)
        buckets[position].append(item)

    res = []
    for bucket in buckets:
        quick_sort(bucket)
        res.extend(bucket)

    return res
