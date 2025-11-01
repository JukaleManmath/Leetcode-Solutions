class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        res = []
        ns = s
        for i in range(1, n+1):
            t = s[:i][::-1] + s[i:]
            ns = min(ns, t)
            t = s[:n-i] + s[n-i:][::-1]
            ns = min(ns, t)
        return ns