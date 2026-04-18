class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = n
        rev = str(rev)
        rev = rev[::-1]
        return abs(n - int(rev))