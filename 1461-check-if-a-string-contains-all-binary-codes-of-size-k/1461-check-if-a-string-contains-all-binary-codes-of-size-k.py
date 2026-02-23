class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        res = set()
        i = 0
        while i + k - 1 < n:
            res.add(s[i:i + k])
            i += 1
        return len(res) == 2 ** k