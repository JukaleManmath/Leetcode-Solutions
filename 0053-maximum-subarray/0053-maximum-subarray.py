class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = float("-inf")
        for i in range(n):
            for j in range(i,n ):
                s = max(s, sum(nums[i:j+1]))
        return s