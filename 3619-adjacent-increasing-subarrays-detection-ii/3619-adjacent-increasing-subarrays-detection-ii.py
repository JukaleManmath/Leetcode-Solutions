class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        inc, prev, res = 1, 0 , 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                prev = inc
                inc = 1
            half = inc >> 1
            k = min(inc, prev)
            m = max(half, k)
            if m > res:
                res = m
        return res
