class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for l in range(n):
            mp = defaultdict(int)
            for r in range(l , n):
                mp[s[r]] += 1
                # if max(mp.values()) == mp[s[r]] and min(mp.values()) == mp[s[r]]:
                if len(set(mp.values())) == 1:
                    if r - l + 1 > res:
                        res = r - l + 1
        return res