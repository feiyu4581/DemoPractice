class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for word in path.strip().split('/'):
            if not word or word == '/' or word == '.':
                continue
            elif word == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(word)

        return '/' + '/'.join(stack)

x = Solution()
print(x.simplifyPath("/home/") == "/home")
print(x.simplifyPath("/a/./b/../../c/") == "/c")
print(x.simplifyPath("/../") == "/")
print(x.simplifyPath("/home//foo/") == "/home/foo")
        