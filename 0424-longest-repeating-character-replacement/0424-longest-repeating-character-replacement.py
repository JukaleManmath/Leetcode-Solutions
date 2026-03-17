class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        mp = defaultdict(int)
        l = 0
        maxf = 0
        res = 0
        for r in range(n):
            mp[s[r]] += 1
            if mp[s[r]] > maxf:
                maxf = mp[s[r]]
            
            while (r - l + 1) - maxf > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res , r - l + 1)
        return res