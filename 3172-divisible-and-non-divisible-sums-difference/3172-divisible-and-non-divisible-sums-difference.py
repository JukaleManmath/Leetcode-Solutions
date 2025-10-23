class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = 0
        for i in range(n+1):
            if i % m != 0:
                total += i
            else:
                total -= i
        return total