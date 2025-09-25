class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = []
        # mp = {}
        # for i in range(len(strs)):
        #     raw = str(sorted(strs[i]))
        #     if raw not in mp:
        #         mp[raw] = [strs[i]]
        #     else:
        #         mp[raw].append(strs[i])
        
        # for i in mp:
        #     res.append(mp[i])
        # return res

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch)- ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        