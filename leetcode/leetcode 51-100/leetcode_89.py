class Solution:
    def grayCode(self, n):
        if n==0:
            return [0]
        res=[0,1]
        for i in range(2,n+1):            
            res.extend([x+2**(i-1) for x in res[::-1]])           
        return res

    def grayCode2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if not n:
            return [0]

        memo = {}
        def compute_next(s):
            nonlocal memo
            if not s:
                return []

            tuple_s = tuple(s)
            if tuple_s not in memo:
                if len(s) == 1:
                    ans = s[0] == '1' and [['0']] or [['1']]
                else:
                    ans = []
                    for result in compute_next(s[1:]):
                        s = s[:1] + result
                        ans.append(list(s))

                    s[0] = s[0] == '1' and '0' or '1'
                    ans.append(s)
                    for result in compute_next(s[1:]):
                        s = s[:1] + result
                        ans.append(s)

                memo[tuple_s] = ans

            return memo[tuple_s]
                    
        def gray(start, index):
            if index == 0:
                yield start
                yield from gray(start, 1)
            elif index <= n:
                for result in compute_next(start[-index:]):
                    start = start[:-index] + result
                    yield start

                index += 1
                if index <= n and start[-index] == '0':
                    start[-index] = '1'
                    yield start
                    yield from gray(start, index - 1)
                else:
                    index += 1
                    if index <= n:
                        start[-index] = '1'
                        yield start
                        yield from gray(start, index - 1)

        res = []
        for x in gray(['0'] * n, 0):
            res.append(int(''.join(x), 2))

        return res


x = Solution()
print(x.grayCode(4))
print(x.grayCode(2) == [0,1,3,2])
print(x.grayCode(0) == [0])
        