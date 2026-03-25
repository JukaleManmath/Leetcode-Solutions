class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        def rec(i):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            take = nums[i] + rec (i - 2)
            notake = rec(i - 1)
            dp[i] = max(take, notake)
            return dp[i]
        return rec(n - 1)