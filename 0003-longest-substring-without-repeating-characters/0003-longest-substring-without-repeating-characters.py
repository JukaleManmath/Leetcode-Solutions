class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mp = {}
        l = r = 0
        longest = -1
        while r < n:
            mp[s[r]] = 1 + mp.get(s[r], 0)
            while mp[s[r]] >= 2:
                mp[s[l]] -= 1
                l += 1   
            longest = max(longest, r - l + 1)
            r += 1
        return longest if longest != -1 else 0
