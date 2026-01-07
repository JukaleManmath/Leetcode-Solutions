class Solution:
    def largestEven(self, s: str) -> str:
        i = len(s) -1
        while i >= 0:
            if s[i] == "2":
                break
            i -= 1
        return s[:i+1]
