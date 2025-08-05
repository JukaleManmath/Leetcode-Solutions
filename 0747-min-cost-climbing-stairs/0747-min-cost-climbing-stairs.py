class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top - Down Memoization
        # n = len(cost)
        # cache = [-1] * (n + 1)

        # def dfs(i):
        #     if i >= n:
        #         return 0
            
        #     if cache[i] != -1:
        #         return cache[i]
            
        #     cache[i] = cost[i] + min(dfs(i + 1), dfs(i +2))
        #     return cache[i]
    
        # return min(dfs(0), dfs(1))

        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i - 2])
        return dp[n]