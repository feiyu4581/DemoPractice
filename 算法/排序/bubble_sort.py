def sort(items):
    for end in range(len(items), 0, -1):
        for start in range(1, end):
            if items[start] < items[start - 1]:
                items[start], items[start - 1] = items[start - 1], items[start]

    return items
