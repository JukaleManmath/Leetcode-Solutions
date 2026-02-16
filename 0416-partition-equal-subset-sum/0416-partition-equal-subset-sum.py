class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        Sum = sum(nums)
        if Sum % 2 != 0:
            return False
        target = Sum // 2

        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(1, target+1):
                
                notake = dp[i - 1][j]
                take = False
                if nums[i] <= j:
                    take = dp[i-1][j - nums[i]]
                dp[i][j] = take or notake
        return dp[n-1][target]
                 