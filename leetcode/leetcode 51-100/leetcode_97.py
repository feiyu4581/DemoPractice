class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        memo = {}
        def match(left, right, target):
            if (left, right, target) not in memo:
                if not left and not right and not target:
                    ans = True

                elif len(left) + len(right) != len(target):
                    ans = False

                elif left and left[0] == target[0] and match(left[1:], right, target[1:]):
                    ans = True

                elif right and right[0] == target[0] and match(left, right[1:], target[1:]):
                    ans = True
                else:
                    ans = False

                memo[left, right, target] = ans

            return memo[left, right, target]

        return match(s1, s2, s3)


x = Solution()
print(x.isInterleave('aabcc', 'dbbca', 'aadbbcbcac') == True)
print(x.isInterleave('aabcc', 'dbbca', 'aadbbbaccc') == False)
print(x.isInterleave(
    'bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa',
    'babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab',
    'babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab'
    ) == False)
