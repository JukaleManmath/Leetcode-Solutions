class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntt = Counter(t)
        n = len(s)
        req = len(cntt)
        mp = defaultdict(int)
        res = ""
        curr = float("inf")
        l ,r = 0, 0
        have = 0
        while r < n:
            mp[s[r]] += 1
            if s[r] in cntt and mp[s[r]] == cntt[s[r]]:
                have += 1

            while have == req:
                if r - l + 1 < curr:
                    curr = r - l + 1
                    res = s[l: r + 1]
                mp[s[l]] -= 1
                if s[l] in cntt and mp[s[l]] < cntt[s[l]]:
                    have -=  1
                l +=1 
            r += 1
        return res
            


