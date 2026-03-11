class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        i = 0
        while 2 ** i <= n:
            i += 1
        return 2 ** i - 1 - n