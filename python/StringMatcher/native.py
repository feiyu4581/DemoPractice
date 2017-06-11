
def _match_str(left, right):
    return left == right


def match(text, pattern):
    res = []
    pattern_len = len(pattern)
    for index in range(len(text)):
        if _match_str(text[index:index + pattern_len], pattern):
            res.append(index)

    return res
