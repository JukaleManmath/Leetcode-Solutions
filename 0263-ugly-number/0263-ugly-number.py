class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def maxdivide(num , b):
            while num % b == 0:
                num = num // b
            
            return num
        
        res = n
        res = maxdivide(res , 2)
        res = maxdivide(res, 3)
        res = maxdivide(res , 5)

        return res == 1
            