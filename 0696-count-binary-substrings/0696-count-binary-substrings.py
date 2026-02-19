class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        one , zero = 0 , 0
        l, r = 0, 0
        ans = 0
        while r < len(s):
            while r < n and s[r] == "0":
                zero += 1
                r += 1
            if zero and one:
                ans += min(zero, one)
            one = 0
            while  r < n and s[r] == "1":
                one += 1
                r += 1
            
            if zero and one:
                ans += min(zero, one)
            zero = 0
        return ans