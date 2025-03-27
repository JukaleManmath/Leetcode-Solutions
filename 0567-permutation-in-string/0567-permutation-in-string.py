class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        s1 = sorted(s1)
        for i in range(m - n + 1):
            check = ""
            for j in range(i , i + n):
                check += s2[j]
            if s1 == sorted(check):
                return True
        return False

        