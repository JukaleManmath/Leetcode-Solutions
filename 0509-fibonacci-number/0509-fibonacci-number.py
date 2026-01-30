class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        def rec(n):
            if n <=1:
                return n
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = rec(n-1) + rec(n-2)
            return dp[n]
        
        dp[n] = rec(n)
        return dp[n]