class Solution:
    def climbStairs(self, n: int) -> int:
        #  Memoization added to recursion - Top-down approach O(n) - space and time
        # steps= [-1] * (n+1)
        # def dfs(i):
        #     if i == 0 or i == 1:
        #         return 1
        #     if steps[i] != -1:
        #         return steps[i]
        #     steps[i] = dfs(i - 1) + dfs(i-2)
        #     return steps[i]
        # return dfs(n)
        

        #  Bottom-up approach O(n) - space and time
        # if n <= 2:
        #     return n
        # dp = [0] * (n+1)
        # dp[1] , dp[2] = 1, 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i- 1] + dp[i-2]
        # return dp[n]

        # Space optimized dp
        one, two = 1, 1  #(0 and 1 steps are assigned val)
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one