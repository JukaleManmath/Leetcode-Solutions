class Solution:
    def numSub(self, s: str) -> int:
        l = r = 0
        n = len(s)
        res = 0
        mod = 10 ** 9 + 7
        while r < n:
            if s[l] == "1":
                while r < n and s[r] == "1":
                    r += 1
                curr = r - l
                res += ((curr * (curr + 1))// 2) % mod
                l = r
            else:
                l += 1
                r += 1
        return res