class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        r = n % 7
        total = 0
        i = 1
        while w:
            total += ((i + 6)*(i + 7))// 2 - abs((i - 1) * (i))// 2
            w -= 1
            i += 1
        total += ((i + r)*(i + r - 1)) // 2 - (i * (i - 1))// 2
        return total
        