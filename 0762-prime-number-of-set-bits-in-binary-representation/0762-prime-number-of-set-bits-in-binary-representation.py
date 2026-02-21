class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # def isprime(n):
        #     if n == 1:
        #         return False
        #     for i in range(2, n // 2 + 1):
        #         if n % i == 0:
        #             return False
        #     return True

        def helper(n):
            prime = {2, 3,5, 7, 11,13,17,19} # because the value of 10 ** 6 lies between 2**19 and 2 **20 so we need prime numbers max till 19
            return n in prime
        
        res = 0
        for i in range(left, right + 1):
            if helper(bin(i).count("1")):
                res += 1
        return res

            