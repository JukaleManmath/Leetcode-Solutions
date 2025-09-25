class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = {}
        for i in range(len(strs)):
            raw = str(sorted(strs[i]))
            if raw not in mp:
                mp[raw] = [strs[i]]
            else:
                mp[raw].append(strs[i])
        
        for i in mp:
            res.append(mp[i])
        return res

        