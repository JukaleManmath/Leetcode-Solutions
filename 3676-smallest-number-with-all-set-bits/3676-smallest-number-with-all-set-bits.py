class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 1
        while True:
            if  2 ** i <= n:
                i += 1
            else:
                break
        return 2 **i - 1