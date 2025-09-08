class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def iszero(n):
            return True if "0" in str(n) else False
        for i in range(1, n):
            j = n - i
            if not iszero(i) and not iszero(j):
                return [i , j]
        





