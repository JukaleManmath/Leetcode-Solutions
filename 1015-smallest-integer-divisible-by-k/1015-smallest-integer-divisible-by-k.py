class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 ==0:
            return -1
        
        curr = 0
        for i in range(1, k + 1):
            curr = curr * 10 + 1
            if curr % k == 0:
                return i
        
        return -1