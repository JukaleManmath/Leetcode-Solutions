class Solution:
    def climbStairs(self, n: int) -> int:
        #  Memoization added to recursion - Top-down approach
        # steps= [-1] * (n+1)
        # def dfs(i):
        #     if i == 0 or i == 1:
        #         return 1
        #     if steps[i] != -1:
        #         return steps[i]
        #     steps[i] = dfs(i - 1) + dfs(i-2)
        #     return steps[i]
        # return dfs(n)
        

        #  Bottom-up approach
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1] , dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i- 1] + dp[i-2]
        return dp[n]