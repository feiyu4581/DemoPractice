def sort(items):
    for left in range(1, len(items)):
        current = items[left]
        index = left
        while index > 0:
            if items[index - 1] <= current:
                break

            items[index] = items[index - 1]
            index -= 1

        items[index] = current

    return items
