class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        p = 1
        res = 1
        for i in range(2, n +1):
            if i & (i - 1) == 0:
                p += 1
            res = res << p
            res = res | i
            res = res % mod
        return res % mod
