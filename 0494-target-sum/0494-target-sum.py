class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        total = sum(nums)
        if total - target < 0 or (total - target)% 2 != 0:
            return 0
        new = (total - target) // 2
        dp = [[-1] *(new + 1) for _ in range(n)]
        def rec(i , t):
            if i == 0:
                if t == 0 and nums[0] == 0:
                    return 2
                if t == 0 or nums[i] == t:
                    return 1
                return 0
            
            if dp[i][t] != -1:
                return dp[i][t]
            nopick = rec(i - 1, t)
            pick = 0
            if nums[i] <= t:
                pick = rec(i - 1, t - nums[i])
            dp[i][t] =  nopick + pick
            return dp[i][t]
        return rec(n-1, new)