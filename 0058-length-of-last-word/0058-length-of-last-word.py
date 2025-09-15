class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # arr = s.split()
        # return len(arr[-1])
        n = len(s)
        r = n -1
        while s[r] == " ":
            r -= 1
        
        l = r
        while l >=0 and s[l] != " ":
            l -= 1
        
        return r - l
