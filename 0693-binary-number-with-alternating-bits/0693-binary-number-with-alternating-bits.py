class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = n & 1
        n = n >> 1
        while n:
            curr = n & 1
            if curr == flag:
                return False
            flag = curr
            n = n >> 1
        
        return True