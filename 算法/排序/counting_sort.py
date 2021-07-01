def sort(items):
    max_data = max(max(items) + 1, 10)

    buckets = [[] for _ in range(max_data)]
    for item in items:
        buckets[item].append(item)

    res = []
    for bucket in buckets:
        res.extend(bucket)

    return res
