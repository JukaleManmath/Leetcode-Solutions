class Solution:
    def rob(self, nums: List[int]) -> int:
        # Memoization
        # n = len(nums)
        # dp = [-1] * (n + 1)
        
        # #recursion
        # def rec(n):
        #     if n < 0:
        #         return 0
        #     if dp[n] != -1:
        #         return dp[n]

        #     dp[n] = max(rec(n-2) + nums[n] , rec(n-1))
        #     return dp[n]
        # return rec(len(nums) - 1)

        # Tabulation -> Bottom -up
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # n = len(nums)
        # dp = [-1] * (n)
        # dp[0] = nums[0]
        # dp[1] = max(dp[0], nums[1])

        # for i in range(2, n):
        #     dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        # return dp[n-1]

        # space optimization
        n = len(nums)
        if n == 0:
            return 0
        prev, prev2 = nums[0], 0
        for i in range(1, n):
            take = nums[i] + prev2
            notake = prev
            curr = max(take, notake)
            prev2 = prev
            prev = curr
        
        return prev
            