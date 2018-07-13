class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
            
        def merge_value(prefix, generate):
            for res in generate:
                yield prefix + res

        def generate_result(left_index, remaining_index):
            if remaining_index <= 0:
                yield ''

            elif left_index == 0:
                yield from merge_value('(', generate_result(left_index + 1, remaining_index - 1))
            elif remaining_index == left_index:
                yield ')' * left_index
            else:
                yield from merge_value('(', generate_result(left_index + 1, remaining_index - 1))
                yield from merge_value(')', generate_result(left_index - 1, remaining_index - 1))

        return [res for res in generate_result(0, n * 2)]


x = Solution()
print (x.generateParenthesis(3))
print (x.generateParenthesis(0))