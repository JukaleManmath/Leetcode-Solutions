class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0

        if n == 1:
            return nums[0]
        dp = [[-1] * 2 for _ in range(n)]

        def rec(i , flag):
            if i  >= n or (i == n- 1 and flag):
                return 0
            if dp[i][flag] != -1:
                return dp[i][flag]

            dp[i][flag] =  max(nums[i] + rec(i + 2, flag), rec(i + 1, flag))
            return dp[i][flag]
        
        return max(rec(0, True), rec(1, False))
            