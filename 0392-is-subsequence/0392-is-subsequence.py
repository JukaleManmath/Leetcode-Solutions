class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i = 0
        # for ch in t:
        #     if i  < len(s) and s[i] == ch:
        #         i += 1
        #     if i == len(s):
        #         return True
        # return  s == t

        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)