class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0

        cost = [0] * n
        for i in range(1, n - 1):
            cost[i] = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
        
        res = 0
        if n % 2 != 0:
            for i in range(1, n, 2):
                res += cost[i]
            return res

        dp = [[-1] * 2 for _ in range(n)]

        def dfs(i, skipped):
            if i >= n - 1:
                return 0
            if dp[i][skipped] != -1:
                return dp[i][skipped] 
            if skipped:
                dp[i][skipped]  =  cost[i] + dfs(i + 2, True)
                return dp[i][skipped] 
            
            dp[i][skipped] = min(cost[i] + dfs(i + 2, False), cost[i] + dfs(i + 3, True))
            return dp[i][skipped] 
            
        return min(dfs(1, False), dfs(2, True))
    