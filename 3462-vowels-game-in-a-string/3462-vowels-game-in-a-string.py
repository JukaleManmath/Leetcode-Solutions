class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = 0
        vowels = "aeiou"
        for ch in s:
            if ch in vowels:
                cnt += 1
        if cnt == 0:
            return False
        return True