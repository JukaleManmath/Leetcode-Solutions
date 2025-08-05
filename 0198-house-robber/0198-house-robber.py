class Solution:
    def rob(self, nums: List[int]) -> int:
        #  Memoization O(n) - Top down
        # n = len(nums)
        # memo =  [-1] * (n+1)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if memo[i] != -1:
        #         return memo[i]
        #     memo[i] =  max(nums[i] + dfs(i +2) , dfs(i + 1))
        #     return memo[i]
        # return dfs(0)

        # DP  - Bottom Up
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
    
        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]
