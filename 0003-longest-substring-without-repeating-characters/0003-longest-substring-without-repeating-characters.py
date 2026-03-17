class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        n = len(s)
        l , r = 0 , 0 
        res = 0
        while r < n:
            mp[s[r]] += 1
            while mp[s[r]] > 1:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
                
