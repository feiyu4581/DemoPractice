from collections import defaultdict


def compute_transition(pattern):
    pattern_len = len(pattern)
    res = []
    for index in range(len(pattern) + 1):
        transition = defaultdict(lambda: 0)
        for char in set(pattern[0:index + 1]):
            next_index = min(pattern_len, index + 1)

            while next_index > 0:
                if pattern[0:next_index] == pattern[index + 1 - next_index:index] + char:
                     break

                next_index -= 1
            transition[char] = next_index

        res.append(transition)

    return res


def match(text, pattern):
    transition = compute_transition(pattern)

    pattern_index, pattern_len = 0, len(pattern)
    res = []
    for index, char in enumerate(text):
        pattern_index = transition[pattern_index][char]

        if pattern_index == pattern_len:
            res.append(index - pattern_len + 1)

    return res
