class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9  + 7
        odd = 4
        even = 5
        def power(x ,p):
            res  = 1
            x %= mod
            while p > 0:
                if p % 2 == 1:
                    res = (res * x) % mod
                x = (x * x) % mod
                p //= 2
            return res

        if n % 2 == 0:
            return (power(odd, (n // 2) ) * power(even, (n // 2))) % mod
        return ((power(even, n // 2 + 1)) * power(odd, (n // 2)) % mod)