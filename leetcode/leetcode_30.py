from collections import Counter, defaultdict


class Solution:
    def pre_handle(self, needle):
        res = [0]
        match_index = 0
        for word in needle[1:]:
            if match_index > 0 and needle[match_index] != word:
                match_index = res[match_index]

            if needle[match_index] == word:
                match_index += 1

            res.append(match_index)

        return res

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        kmp_lists = self.pre_handle(needle)

        needle_index = 0
        res = []
        for index, word in enumerate(haystack):
            if word == needle[needle_index]:
                needle_index += 1
            else:
                while needle_index > 0 and word != needle[needle_index]:
                    needle_index = kmp_lists[needle_index - 1]

                if word == needle[needle_index]:
                    needle_index += 1

            if needle_index == len(needle):
                res.append((index - needle_index + 1, index))
                needle_index = kmp_lists[needle_index - 1]

        return res

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        location_maps = {}
        for index, word in enumerate(words):
            for location in self.strStr(s, word):
                location_maps.setdefault(location, [])
                location_maps[location].append(index)

        locations = list(sorted(location_maps.keys()))


        res = []
        if locations:
            matchs, exists_words = [locations[0]], [location_maps[locations[0]]]
            index = 1
            while index < len(locations):
                if len(matchs) == len(words):
                    res.append(matchs[0][0])
                    matchs = matchs[1:]
                    exists_words = exists_words[1:]

                if matchs[-1][1] == locations[index][0] - 1:
                    if location_maps[locations[index]] in exists_words:
                        exists_index = exists_words.index(location_maps[locations[index]])
                        matchs = matchs[exists_index + 1:]
                        exists_words = exists_words[exists_index + 1:]
                    matchs.append(locations[index])
                    exists_words.append(location_maps[locations[index]])
                else:
                    matchs = [locations[index]]
                    exists_words.append(location_maps[locations[index]])

                index += 1

            if len(matchs) == len(words):
                res.append(matchs[0][0])

        return res

    def findSubstring2(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        location_maps = {}
        for index, word in enumerate(words):
            for location in self.strStr(s, word):
                location_maps.setdefault(location, [])
                location_maps[location].append(index)

        locations = list(sorted(location_maps.keys()))

        res = []
        def match(matchs, exists_words, index):
            nonlocal locations, location_maps, res

            if len(matchs) == len(words):
                res.append(matchs[0][0])
                matchs = matchs[1:]
                exists_words = exists_words[1:]

            if index >= len(locations):
                return

            if matchs and matchs[-1][1] == locations[index][0] - 1:
                for location_index in location_maps[locations[index]]:
                    if location_index in exists_words:
                        exists_index = exists_words.index(location_index)
                        match(matchs[exists_index + 1:] + [locations[index]], exists_words[exists_index + 1:] + [location_index], index + 1)
                    else:
                        match(matchs + [locations[index]], exists_words + [location_index], index + 1)
            else:
                if matchs and matchs[-1][1] >= locations[index][0] - 1:
                    match(matchs, exists_words, index + 1)

                for location_index in location_maps[locations[index]]:
                    match([locations[index]], [location_index], index + 1)

        if locations:
            for location_index in location_maps[locations[0]]:
                match([locations[0]], [location_index], 1)

        return list(set(res))

    def findSubString3(self, s, words):
        res = []
        if not words:
            return res

        all_words = dict.fromkeys(words, 0)
        for word in words:
            all_words[word] += 1

        words_length = len(words)
        word_len = len(words[0])
        for index in range(len(s) - words_length * word_len + 1):
            currents = dict.fromkeys(words, 0)
            count = 0

            for k in range(0, words_length):
                current = s[index + k * word_len: index + (k + 1) * word_len]
                if current in all_words:
                    currents[current] += 1
                    if currents[current] > all_words[current]:
                        break

                    count += 1
                else:
                    break

            if count == words_length:
                res.append(index)

        return res

    def findSubString4(self, s, words):
        res = []
        if not words:
            return res

        words_len, word_len = len(words) * len(words[0]), len(words[0])
        words_count = Counter(words)
        for step in range(word_len):
            start, current_count = step, Counter()
            for index in range(step, len(s) - word_len + 1, word_len):
                current = s[index: index + word_len]

                if current in words_count:
                    current_count[current] += 1
                    while current_count[current] > words_count[current]:
                        current_count[s[start:start + word_len]] -= 1
                        start += word_len
                else:
                    current_count.clear()
                    start = index + word_len

                if index - start + word_len == words_len:
                    res.append(start)

        return res



x = Solution()
print (x.findSubString4('barfoothefoobarman', ["foo","bar"]))
print (x.findSubString3('barfoothefoobarman', ["foo","bar"]))
print (x.findSubString4('mississippi', ["is"]))
print (x.findSubString3('mississippi', ["is"]))
print (x.findSubString4('aaaaaaaa', ["aa","aa","aa"]))
print (x.findSubString3('aaaaaaaa', ["aa","aa","aa"]))
print (x.findSubString4('wordgoodstudentgoodword', ["word","student"]))
print (x.findSubString3('wordgoodstudentgoodword', ["word","student"]))
print (x.findSubString4('wordgoodgoodgoodbestword', ["word","good","best","word"]))
print (x.findSubString3('wordgoodgoodgoodbestword', ["word","good","best","word"]))
print (x.findSubString4('barfoofoobarthefoobarman', ["bar","foo","the"]))
print (x.findSubString3('barfoofoobarthefoobarman', ["bar","foo","the"]))
print (x.findSubString4('wordgoodgoodgoodbestword', ["word","good","best","good"]))
print (x.findSubString3('wordgoodgoodgoodbestword', ["word","good","best","good"]))
print (x.findSubString4('lingmindraboofooowingdingbarrwingmonkeypoundcake', ["fooo","barr","wing","ding","wing"]))
print (x.findSubString3('lingmindraboofooowingdingbarrwingmonkeypoundcake', ["fooo","barr","wing","ding","wing"]))
print (x.findSubString4('ababaab', ["ab","ba","ba"]))
print (x.findSubString3('ababaab', ["ab","ba","ba"]))
print (x.findSubString4('ababaab', ["ab","ba"]))
print (x.findSubString3('ababaab', ["ab","ba"]))