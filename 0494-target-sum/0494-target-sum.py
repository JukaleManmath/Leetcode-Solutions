class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        total = sum(nums)
        if total - target < 0 or (total - target)% 2 != 0:
            return 0
        new = (total - target) // 2
        # dp = [[0] *(new + 1) for _ in range(n)]
        # def rec(i , t):
        #     if i == 0:
        #         if t == 0 and nums[0] == 0:
        #             return 2
        #         if t == 0 or nums[i] == t:
        #             return 1
        #         return 0
            
        #     if dp[i][t] != -1:
        #         return dp[i][t]
        #     nopick = rec(i - 1, t)
        #     pick = 0
        #     if nums[i] <= t:
        #         pick = rec(i - 1, t - nums[i])
        #     dp[i][t] =  nopick + pick
        #     return dp[i][t]
        # return rec(n-1, new)

        prev = [0] * (new + 1)
        
        prev[0] = 2 if nums[0] == 0 else 1
        if nums[0] != 0 and nums[0] <= new:
            prev[nums[0]] = 1
        
        for i in range(1, n):
            curr = [0] * (new + 1)
            for j in range(new + 1):
                nopick = prev[j]
                pick = 0
                if nums[i] <= j:
                    pick = prev[j - nums[i]]
                curr[j] = pick + nopick
            prev = curr
        return prev[new]

        