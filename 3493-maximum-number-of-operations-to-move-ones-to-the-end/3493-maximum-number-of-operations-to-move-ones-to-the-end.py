class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0
        num1 = 0
        while i < n:
            if s[i] == "0":
                res += num1
                while i < n and s[i] != "1":
                    i += 1
            num1 += 1
            i += 1
        return res