class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            res = 0
            while n:
                res += 1 if n & 1 else 0
                n = n >> 1
            return res
        
        ans = []
        for i in range(n+1):
            ans.append(count(i))
        return ans