class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(n):
            if n == 1:
                return False
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    return False
            return True
        
        res = 0
        for i in range(left, right + 1):
            if isprime(bin(i).count("1")):
                res += 1
        return res

            