class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l , r = 0, 0
        minlen = float("inf")
        curr = 0
        while r < n:
            curr += nums[r]
            while curr >= target:
                minlen = min(minlen, r -l+1)
                curr -= nums[l]
                l += 1
            r += 1
        return minlen if minlen != float("inf") else 0
            


 