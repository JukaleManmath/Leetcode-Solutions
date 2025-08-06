class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
                return nums[0]

        def helper(num):
            if not num:
                return 0
            if len(num) == 1:
                return num[0]
            dp = [0] * (len(num))
            dp[0] = num[0]
            dp[1] = max(num[0], num[1])
            for i in range(2, len(num)):
                dp[i] = max( dp[i-1], num[i] + dp[i - 2])
            return dp[-1]
        return max(helper(nums[1:]) , helper(nums[:-1]))
