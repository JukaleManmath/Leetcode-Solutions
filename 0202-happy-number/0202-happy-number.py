class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            res = 0
            while n:
                res += (n% 10) ** 2
                n //= 10
            return res
        
        seen = []
        while True:
            n = square(n)
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.append(n)

            

                
