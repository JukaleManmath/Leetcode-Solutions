class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1 = Counter(t)
        mp2 = defaultdict(int)
        char = set(t)
        n = len(s)
        start, end = 0, 0
        minlen = n + 1
        res = ""
        l = 0
        required = len(mp1)
        have = 0
        for r in range(n):
            mp2[s[r]] += 1
            if s[r] in char:
                if mp2[s[r]] == mp1[s[r]]:
                    have +=1
            
            while have == required:
                if minlen > r - l + 1:
                    minlen = r - l + 1
                    res = s[l:r +1]
                mp2[s[l]] -= 1
                if s[l] in char and mp2[s[l]] < mp1[s[l]]:
                    have -= 1
                l += 1
        return res
                    
