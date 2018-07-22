class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def permutation(s, sequence):
            s.sort()
            if sequence <= 1:
                return s

            current_sequence = 1
            for index in range(1, len(s) + 1):
                last_sequence = current_sequence
                current_sequence *= index
                if current_sequence == sequence:
                    return s[0:len(s) - index] + sorted(s[len(s) - index:], reverse=True)

                if current_sequence > sequence:
                    current_sequence = last_sequence
                    i = index
                    while current_sequence < sequence:
                        current_sequence += last_sequence
                        i -= 1

                    s[len(s) - index], s[len(s) - i] = s[len(s) - i], s[len(s) - index]
                    return s[0:len(s) - index + 1] + permutation(s[len(s) - index + 1:], sequence - current_sequence + last_sequence)

        s = [str(index) for index in range(1, n + 1)]
        res = permutation(s, k)
        return ''.join(res)


x = Solution()
print(x.getPermutation(3, 2) == '132')
print(x.getPermutation(3, 4) == '231')
print(x.getPermutation(3, 3) == '213')
print(x.getPermutation(4, 9) == '2314')
print(x.getPermutation(4, 14) == '3142')
        