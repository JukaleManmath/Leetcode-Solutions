class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        res  = 0
        buy = nums[0]

        for i in range(1, len(nums)):
            if buy > nums[i]:
                buy = nums[i]
            res = max(res, nums[i] - buy)
        return res