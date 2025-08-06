class Solution:
    def rob(self, nums: List[int]) -> int:
        #  Bottom up approach max( 1 - n-1 house , 2- n houses) as n and 1 houses are adjacent
        # n = len(nums)
        # if n == 1:
        #         return nums[0]

        # def helper(num):
        #     if not num:
        #         return 0
        #     if len(num) == 1:
        #         return num[0]
        #     dp = [0] * (len(num))
        #     dp[0] = num[0]
        #     dp[1] = max(num[0], num[1])
        #     for i in range(2, len(num)):
        #         dp[i] = max( dp[i-1], num[i] + dp[i - 2])
        #     return dp[-1]
        # return max(helper(nums[1:]) , helper(nums[:-1]))

        # memoization - Top down
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        memo = [[-1] * 2 for _ in range(len(nums))]
        def dfs(i , flag):
            if i >= len(nums) or (flag and i == len(nums)-1):
                return 0
            
            if memo[i][flag] != -1:
                return memo[i][flag]
            
            memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))
            return memo[i][flag]
        return max(dfs(0 , True), dfs(1, False))
            