class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0
        num1 = 0
        while i < n - 1:
            if s[i] == "1" and s[i+ 1] == "0":
                i += 1
                num1 += 1
                while i < n and s[i] != "1":
                    i += 1
                res += num1
            elif s[i] == "1" and s[i+1] == "1":
                i += 1
                num1 += 1
            else:
                i += 1
        return res