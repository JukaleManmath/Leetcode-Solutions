class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = {}
        c = {}
        vowels = "aeiou"
        mv, mc = 0, 0
        for ch in s:
            if ch in vowels:
                v[ch] = 1 + v.get(ch, 0)
            else:
                c[ch] = 1 + c.get(ch, 0)

        for ch in v:
            mv = max(mv, v[ch])
        
        for ch in c:
            mc = max(mc, c[ch])
        return mv + mc
                