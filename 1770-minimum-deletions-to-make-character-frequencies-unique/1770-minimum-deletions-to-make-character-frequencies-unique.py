class Solution:
    def minDeletions(self, s: str) -> int:
        sc = {}
        for ch in s:
            sc[ch] = sc.get(ch, 0) + 1
        res = []
        for i in sc:
            res.append(sc[i])
        res.sort()
        n = 0
        for i in range(len(res)-2, -1, -1):
            if res[i] >= res[i+1]:
                prev= res[i]
                res[i] = max(0, res[i+1] -1)
                n += prev - res[i]
        return n