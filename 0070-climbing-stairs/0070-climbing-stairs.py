class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def rec(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = rec(n-1) + rec(n-2)
            return dp[n]
        
        return rec(n)