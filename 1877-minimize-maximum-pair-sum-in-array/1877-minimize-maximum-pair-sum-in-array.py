class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n % 2 != 0:
            return 0
        nums.sort()
        maxsum = float("-inf")
        for i in range(n//2):
            maxsum = max(maxsum, nums[i] + nums[n - i- 1])
        return maxsum