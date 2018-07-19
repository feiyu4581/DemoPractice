class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = self.prime()
        res = {}
        str_map = {}
        for word in strs:
            num = 1
            for char in word:
                if char not in str_map:
                    str_map[char] = next(prime)

                num *= str_map[char]

            res.setdefault(num, [])
            res[num].append(word)

        return list(res.values())

    def prime(self):
        prime_list = [2]
        yield 2
        index = 3
        while True:
            for num in prime_list:
                if index % num == 0:
                    break
                elif num ** 2 > index:
                    yield index
                    prime_list.append(index)
                    break
            else:
                yield index
                prime_list.append(index)

            index += 2



x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
])
        