class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, state = [], []
        def restore(remaining_s):
            nonlocal res, state
            if len(remaining_s) > (4 - len(state)) * 3:
                return
            
            if len(state) == 3:
                if remaining_s and int(remaining_s) <= 255:
                    if len(remaining_s) == 1 or remaining_s[0] != '0':
                        res.append(state + [remaining_s])
            elif remaining_s:
                state.append(remaining_s[0:1])
                restore(remaining_s[1:])
                state.pop()

                if len(remaining_s) >= 2 and remaining_s[0] != '0':
                    state.append(remaining_s[0:2])
                    restore(remaining_s[2:])
                    state.pop()

                if len(remaining_s) >= 3 and remaining_s[0] != '0' and int(remaining_s[:3]) <= 255:
                    state.append(remaining_s[0:3])
                    restore(remaining_s[3:])
                    state.pop()

        restore(s)
        print (res)
        return list(map(lambda item: '.'.join(item), res))
            


x = Solution()
print(x.restoreIpAddresses("25525511135") == [
    "255.255.11.135",
    "255.255.111.35"
])

print(x.restoreIpAddresses("010010") == [
    "0.10.0.10",
    "0.100.1.0"
])
        