class Solution:
    def hasSameDigits(self, s: str) -> bool:
        total = 0
        while len(s) > 2:
            news = ""
            for i in range(len(s)-1):
                news += str((int(s[i]) + int(s[i+1])) % 10)
            s = news
        return s[0] == s[1]