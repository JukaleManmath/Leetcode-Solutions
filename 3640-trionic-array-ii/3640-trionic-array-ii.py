class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[None for _ in range(4)] for _ in range(n)]
        def rec(i , status):
            if i == n:
                return 0 if status == 3 else float("-inf")
            if dp[i][status] is not None:
                return dp[i][status]
            take = float("-inf")
            notake = float("-inf")
            if status == 0:
                notake = rec(i + 1, 0)

            if status == 3:
                take = nums[i]
            
            if i + 1 < n:
                if status == 0:
                    if nums[i + 1] > nums[i]:
                        take = max(take, nums[i] + rec(i + 1, 1))
                elif status == 1:
                    if nums[i + 1] > nums[i]:
                        take = max(take, nums[i] + rec(i + 1, 1))
                    elif nums[i + 1] < nums[i]:
                        take = max(take, nums[i] + rec(i + 1, 2))
                elif status == 2:
                    if nums[i + 1] < nums[i]:
                        take = max(take, nums[i] + rec(i + 1, 2))
                    elif nums[i + 1] > nums[i]:
                        take = max(take, nums[i] + rec(i + 1, 3))
                elif status == 3:
                    if nums[i + 1] > nums[i]:
                        take = max(take, nums[i] + rec(i + 1, 3))      

            dp[i][status]=  max(take, notake)
            return dp[i][status]
        return rec(0, 0) 

            