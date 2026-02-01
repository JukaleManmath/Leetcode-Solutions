class Solution:
    def rob(self, nums: List[int]) -> int:
        # Memoization
        n = len(nums)
        dp = [-1] * (n + 1)
        
        #recursion
        def rec(n):
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]

            dp[n] = max(rec(n-2) + nums[n] , rec(n-1))
            return dp[n]
        return rec(len(nums) - 1)