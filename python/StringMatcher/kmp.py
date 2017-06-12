
def precompute_str(seq):
    res = [0]
    match_index = 0
    for char in seq[1:]:
        while match_index > 0 and char != seq[match_index]:
            match_index = res[match_index]

        if char == seq[match_index]:
            match_index += 1

        res.append(match_index)

    return res


def match(text, pattern):
    pre_matchs = precompute_str(pattern)
    pattern_index = 0

    res = []
    for index, char in enumerate(text):
        if pattern[pattern_index] == char:
            pattern_index += 1
        else:
            pattern_index = pre_matchs[pattern_index - 1]

        if pattern_index == len(pattern):
            res.append(index)

    return res
