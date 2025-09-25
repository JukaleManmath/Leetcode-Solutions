class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sm , tm = Counter(s), Counter(t)
        mp = {}
        for chs, cht in zip(s , t):
            if sm[chs] != tm[cht] or (chs in mp and mp[chs] != cht):
                return False
            mp[chs] = cht
        return True

        