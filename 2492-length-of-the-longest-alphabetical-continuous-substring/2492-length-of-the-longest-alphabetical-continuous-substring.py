class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        def getvalue(ch):
            return ord(ch) - ord('a')
        
        n = len(s)
        if n == 1:
            return 1
        l = r = 0

        maxlen = 1
        while r < n - 1:
            if getvalue(s[r+1]) - getvalue(s[r]) == 1:
                r = r + 1
                maxlen = max(maxlen, r -l + 1)
            else:
                r = r + 1
                l = r 
            
        return maxlen