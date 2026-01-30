class Solution:
    def fib(self, n: int) -> int:
        # memoization -> top -down approach. from answer -> base case
        # dp = [-1] * (n+1)
        # def rec(n):
        #     if n <=1:
        #         return n
            
        #     if dp[n] != -1:
        #         return dp[n]
            
        #     dp[n] = rec(n-1) + rec(n-2)
        #     return dp[n]
        
        # return rec(n)

        # tabulation ->. bottom up -> from base case to answer
        if n <= 1:
            return n
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]