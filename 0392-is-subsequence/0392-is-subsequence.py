class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i  < len(s) and s[i] == ch:
                i += 1
            if i == len(s):
                return True
        return  s == t