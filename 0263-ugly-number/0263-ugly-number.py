class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def maxdivide(num , b):
            aa = num
            while aa % b == 0:
                aa = aa // b
            
            return aa
        
        res = n
        res = maxdivide(res , 2)
        res = maxdivide(res, 3)
        res = maxdivide(res , 5)

        return res == 1
            