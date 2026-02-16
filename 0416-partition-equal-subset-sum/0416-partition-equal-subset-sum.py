class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        Sum = sum(nums)
        if Sum % 2 != 0:
            return False
        target = Sum // 2

        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
        def rec(i,  tar):
            if tar == 0:
                return True
            if i >= n:
                return False
            if dp[i][tar] != -1:
                return dp[i][tar]
            
            take = rec(i + 1, tar - nums[i])
            notake = rec(i + 1, tar)

            dp[i][tar] =  take or notake
            return dp[i][tar]
        return rec(0, target)