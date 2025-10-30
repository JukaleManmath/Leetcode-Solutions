class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = 0
        for i in s:
            total += ord(i)  - ord('a') + 1
        ps = 0
        for i in s:
            ps += ord(i)  - ord('a') + 1
            if ps * 2 == total:
                return True
        return False