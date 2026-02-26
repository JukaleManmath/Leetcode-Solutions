class Solution:
    def numSteps(self, s: str) -> int:
        curr = int(s, 2)
        res = 0
        
        while curr != 1:
            if (curr & 1) == 0:
                curr = curr // 2
            else:
                curr += 1
                
            res += 1
        return res