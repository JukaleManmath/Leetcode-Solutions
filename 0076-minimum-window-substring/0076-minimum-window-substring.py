class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        countt = Counter(t)
        window= {}
        need = len(countt)
        have = 0
        n = len(s)
        l = 0
        minlen = n + 1
        res = ""
        for i in range(n):
            ch = s[i]
            window[ch] = window.get(ch, 0) + 1

            if ch in t and window[ch] == countt[ch]:
                have += 1

            while have == need:
                if i - l + 1 < minlen:
                    minlen = i - l + 1
                    res = s[l : i + 1]
                
                window[s[l]] -= 1
                if s[l] in t and window[s[l]] < countt[s[l]]:
                    have -= 1
                l += 1
            
        return res



                 
