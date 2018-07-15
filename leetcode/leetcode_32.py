class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res, sequence, max_sequence = {}, 0, 0
        for index, w in enumerate(s):
            if w == '(':
                stack.append(index)
                sequence += 1
                max_sequence += 1
            elif w == ')' and stack:
                before_index = stack.pop()
                res[(before_index, index)] = index - before_index + 1
                sequence -= 1

                if not sequence:
                    max_sequence = 0

        max_result = 0
        if res:
            keys = list(sorted(res.keys()))
            prev = keys[0]
            max_result = res[prev]
            for key in keys[1:]:
                if prev[1] >= key[0]:
                    continue
                elif prev[1] + 1 == key[0]:
                    next_prev = (prev[0], key[1])
                    res[next_prev] = res[prev] + res[key]
                    prev = next_prev
                    max_result = max(res[next_prev], max_result)
                else:
                    prev = key
                    max_result = max(res[prev], max_result)


        return max_result

    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        index = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    index = i + 1
                else:
                    stack.pop()
                    if len(stack) == 0:
                        result = max(result, i-index+1)
                    else:
                        result = max(result, i-stack[-1])
        return result
        
x = Solution()
print(x.longestValidParentheses2('(()') == 2)
print(x.longestValidParentheses2(')()())') == 4)
print(x.longestValidParentheses2('()(()') == 2)
print(x.longestValidParentheses2(')()())()()(') == 4)
print(x.longestValidParentheses2('(()())()()(') == 10)
print(x.longestValidParentheses2(')(()((((())') == 4)