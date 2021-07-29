def sort(items):
    for i in range(len(items)):
        min_value, min_index = None, -1
        for index in range(i, len(items)):
            if min_value is None or items[index] < min_value:
                min_value, min_index = items[index], index

        items[i], items[min_index] = items[min_index], items[i]

    return items
