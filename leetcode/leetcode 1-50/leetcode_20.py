class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_maps = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        keys, values = valid_maps.keys(), valid_maps.values()
        stacks = []
        for w in s:
            if w in keys:
                stacks.append(w)
            elif w in values:
                if stacks and valid_maps[stacks.pop()] == w:
                    continue
                return False
        return not bool(stacks)


x = Solution()
print (x.isValid('()') == True)
print (x.isValid('()[]{}') == True)
print (x.isValid('(]') == False)
print (x.isValid('([)]') == False)
print (x.isValid('{[]}') == True)
print (x.isValid('}{[]}') == False)
print (x.isValid(']') == False)
print (x.isValid('[') == False)