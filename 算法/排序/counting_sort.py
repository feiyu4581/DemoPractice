def sort(items, key=lambda item: item):
    max_data = max(max([key(item) for item in items]) + 1, 10)

    buckets = [[] for _ in range(max_data)]
    for item in items:
        buckets[key(item)].append(item)

    res = []
    for bucket in buckets:
        res.extend(bucket)

    return res
