class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # naive with sorting
        # mp = {}

        # n = len(strs)
        # for i in range(n):
        #     curr = "".join(sorted(strs[i]))
        #     if curr in mp:
        #         mp[curr].append(strs[i])
        #     else:
        #         mp[curr] = [strs[i]]
        # return list(mp.values())

        res = defaultdict(list)
        for i in range(len(strs)):
            cnt = [0] * 26
            for c in strs[i]:
                cnt[ord(c) - ord('a')] += 1
            res[tuple(cnt)].append(strs[i])
        return list(res.values())
