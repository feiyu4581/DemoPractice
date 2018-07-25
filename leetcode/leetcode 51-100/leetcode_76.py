from collections import Counter

class Solution:
    def minWindow(self, s, t):
        need, missing = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return ''

        if len(t) == 1 and t in s:
            return t

        res = {}
        min_s = None
        t_counter = Counter(t)
        for index in range(0, len(s)):
            res[index, index] = s[index] in t and 1 or 0

        for i in range(0, len(s)):
            counter = Counter(s[i])
            for j in range(i + 1, len(s)):
                if min_s and min_s[1] - min_s[0] < j - i:
                    continue

                if s[j] in t_counter and t_counter[s[j]] > counter[s[j]]:
                    counter[s[j]] += 1
                    res[i, j] = res[i, j - 1] + 1
                    if res[i, j] == len(t):
                        if not min_s or j - i < min_s[1] - min_s[0]:
                            min_s = (i, j)

                        break
                else:
                    res[i, j] = res[i, j - 1]
                    
        if min_s:
            return s[min_s[0]:min_s[1] + 1]

        return ''
    

x = Solution()
# print(x.minWindow('ADOBECODEBANC', 'ABC') == 'BANC')
# print(x.minWindow('aa', 'aa') == 'aa')
print(x.minWindow('wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon', 'ozgzyywxvtublcl'))
print(x.minWindow('hwffmpuhbqftfeqfsyvwbrxwbgzalhfselzsctbdmgzrnpzfnwdonakoilrutwozjormjurvaspphouwkzmxczokkfgddvcplvdupussphhwxethdfgfeusrbyufvzugwzdmvvgkenhbtckzjqeqnyhoxbvscrbzqenmbtwfifiejudtkjjziqqhtlzwdcxtikhjfgqpnatxuwqfgbgqtwxmiyklbhgjtqvywlojmhiggynobweusbjcztpadwmwmhxkultgucpcceqgauatvlvxfnzkjlgxudhpqcxngmpltgrtctoafmxmzwwkkcheiqvystlbhdoajfwnaknfwktvjpftuozcevczoqcxtqyevurxgffdryaaoivkyvmdsqeiggfbwfhtbzqigvlxunakxxuwuibmafujnckjhscjturzqeymtywrwspscqfcxblkdwtlqxwlrpkjvkvolthjlwbnogqlibvnzqyrpwchlosgboxmhevvbwkrfcdpgachrdzizdrnukvvysjhxeeacprjtwyzxdhqgiyhlswhcsccklljrqlwhdfabgcyjjqprryejvmlnopzcajtsupzzxcbdgbmpudilbmwyajlryltawotqgusdytgewutqxddaqbzqkkhkxcltrgmzagczzkdxgzqdctfuxenhrwuqzhmsnyr', 'pgvofhuentu'))
print(x.minWindow('gxkvmymaztebptcdhquxemoowthbmzluwvpivdiuwoxmjzrqrmpyyemwxwylxlhtiwddcnyycvmnxeeoqtmqzbnzznkwyuriqulujjtnhfbejfubahsckhbjwnfwhweaspubbnpivsogxiizrcbdjemfstdzrhzjwwnzjehgwxnvivwzzadkerpyluyebzozxdzhjipficcqzyryauifozdbtdfwfvwcyxlhhbopfsfhtxfttqahrginlqjslhxkektonkdtcjavihrdxrnrxxejnndzvajblepyqvrtgtqobhtabgraevjrlpqipbjaibzyystemkuptnruujvaggrrvkznnlnvoowmjpsxbmmvbdrxooxxxrqudshqfxotnkhwzztbnfyqlpobgladerzhjjyogojtyssxtlagtywgqmhwyibezamkjmarajnabfxuqacjyaponzmnhnriofuzturvfevgjvczvglviamvzykimesalmbfisanwyvhtxjqfulowxlwyygkczmnnnuwixjgvfoqexgmttaptnnrludpvpfiezemwqttxjjbirnblpqgfgzqacixtnfxmmmlefebqoeyfuzsjryqxzjzbrwweeusqgdunixdybddv', 'eyhvyxvygwb'))
        