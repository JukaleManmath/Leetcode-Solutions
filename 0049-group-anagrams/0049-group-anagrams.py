class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        n = len(strs)
        for i in range(n):
            curr = "".join(sorted(strs[i]))
            if curr in mp:
                mp[curr].append(strs[i])
            else:
                mp[curr] = [strs[i]]
        return list(mp.values())