class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = {}
        def distance(left, right):
            if (left, right) not in memo:
                if left == 0:
                    ans = right

                elif right == 0:
                    ans = left

                elif word1[left - 1] == word2[right - 1]:
                    ans = distance(left - 1, right - 1)
                else:
                    ans = min(distance(left - 1, right) + 1, distance(left, right - 1) + 1, distance(left - 1, right - 1) + 1)

                memo[left, right] = ans

            return memo[left, right]

        return distance(len(word1), len(word2))
    

x = Solution()
print(x.minDistance('horse', 'ros') == 3)
print(x.minDistance('intention', 'execution') == 5)
print(x.minDistance('dinitrophenylhydrazine', 'benzalphenylhydrazone') == 7)