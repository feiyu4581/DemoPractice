class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n - 1):
            current_num = res[0]
            current_index = 1
            new_res = ''
            for num in res[1:]:
                if num == current_num:
                    current_index += 1
                else:
                    new_res += '{}{}'.format(current_index, current_num)
                    current_num, current_index = num, 1

            res = new_res
            res += '{}{}'.format(current_index, current_num)

        return res
    
x = Solution()
print (x.countAndSay(1) == '1')
print (x.countAndSay(2) == '11')
print (x.countAndSay(3) == '21')
print (x.countAndSay(4) == '1211')
print (x.countAndSay(5) == '111221')
print (x.countAndSay(6) == '312211')
print (x.countAndSay(7) == '13112221')
