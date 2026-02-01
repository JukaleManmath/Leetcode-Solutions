class Solution:
    def canCross(self, stones: List[int]) -> bool:
        mp = {}
        n = len(stones)
        for i in range(len(stones)):
            mp[stones[i]] = i

        dp = [[-1] * n for _ in range(n)]
        def rec(idx , k):
            if idx == n - 1:
                return True
            
            if dp[idx][k] != -1:
                return dp[idx][k] == 1

            k0 , k1 , k2 = False, False, False

            if stones[idx] + k in mp:
                k0 = rec(mp[stones[idx] + k], k)
            if k > 1 and stones[idx] + k -1 in mp:
                k1 = rec(mp[stones[idx] + k - 1], k -1)
            if stones[idx] + k + 1 in mp:
                k2 = rec(mp[stones[idx] + k + 1], k + 1)
            
            dp[idx][k] = 1 if k0 or k1 or k2 else 0
            return dp[idx][k] == 1
        
        if stones[1] - stones[0] != 1:
            return False
        
        return rec(1,1)
        
