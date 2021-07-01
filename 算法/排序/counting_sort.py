def sort(items, key=lambda item: item):
    max_data = max(max([key(item) for item in items]) + 1, 10)

    buckets = [[] for _ in range(max_data)]
    for item in items:
        buckets[key(item)].append(item)

    res = []
    for bucket in buckets:
        res.extend(bucket)

    return res


def sort_with_counting(items, key=lambda item: item):
    max_data = max(max([key(item) for item in items]) + 1, 10)

    buckets = [0 for _ in range(max_data)]
    for item in items:
        buckets[key(item)] += 1

    for index in range(1, len(buckets)):
        buckets[index] += buckets[index - 1]

    res = [None for _ in range(len(items))]
    for item in reversed(items):
        buckets[key(item)] -= 1
        res[buckets[key(item)]] = item

    return res
