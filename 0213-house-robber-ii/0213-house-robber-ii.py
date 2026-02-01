class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top -down / Memoization
        # n = len(nums)
        # if not nums:
        #     return 0

        # if n == 1:
        #     return nums[0]
        # dp = [[-1] * 2 for _ in range(n)]

        # def rec(i , flag):
        #     if i  >= n or (i == n- 1 and flag):
        #         return 0
        #     if dp[i][flag] != -1:
        #         return dp[i][flag]

        #     dp[i][flag] =  max(nums[i] + rec(i + 2, flag), rec(i + 1, flag))
        #     return dp[i][flag]
        
        # return max(rec(0, True), rec(1, False))

        # Bottom-up / Tabulation
        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return nums[0]
        
        # def helper(arr):
        #     m = len(arr)
        #     dp = [-1] * (m)
        #     dp[0] = arr[0]
        #     for i in range(1, m):
        #         take = arr[i]
        #         if i > 1:
        #             take += dp[i - 2]
        #         notake = dp[i - 1]
        #         dp[i] = max(take, notake)
        #     return dp[m -1]
        
        # return max(helper(nums[:-1]), helper(nums[1:]))


        # space optimized - O(1) & time -> same  O(n)
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        def helper(arr):
            m = len(arr)
            prev = arr[0]
            prev2 = 0
            for i in range(1, m):
                take = arr[i] + prev2
                notake = prev
                curr = max(take, notake)
                prev2 = prev
                prev = curr
            return prev
        
        return max(helper(nums[:-1]), helper(nums[1:]))

