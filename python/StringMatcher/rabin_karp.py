import math

MOD_NUM = 123


def get_str_map(seq):
    res = {}
    index = 0
    for char in set(seq):
        res[char] = index
        index += 1

    return res, index


def match(text, pattern):
    text_len, pattern_len = len(text), len(pattern)
    str_map, d = get_str_map(text + pattern)
    h = math.pow(d, pattern_len - 1) % MOD_NUM

    pattern_num, text_num = str_map[pattern[0]] % MOD_NUM, str_map[text[0]] % MOD_NUM

    for index in range(1, pattern_len):
        pattern_num = (d * pattern_num + str_map[pattern[index]]) % MOD_NUM
        text_num = (d * text_num + str_map[text[index]]) % MOD_NUM

    text_nums = [text_num]

    res = []
    for index in range(text_len - pattern_len + 1):
        if pattern_num == text_nums[index]:
            if pattern == text[index:index + pattern_len]:
                res.append(index)

        if index < text_len - pattern_len:
            text_nums.append(
                (d * (text_nums[-1] - str_map[text[index]] * h) + str_map[text[index + pattern_len]]) % MOD_NUM
            )

    return res
