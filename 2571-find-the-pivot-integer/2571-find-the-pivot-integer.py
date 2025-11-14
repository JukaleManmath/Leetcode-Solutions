class Solution:
    def pivotInteger(self, n: int) -> int:
        def s(num):
            return (num * (num + 1))// 2
        for i in range(1, n+1):
            if s(i) == s(n) - s(i-1):
                return i
        return -1