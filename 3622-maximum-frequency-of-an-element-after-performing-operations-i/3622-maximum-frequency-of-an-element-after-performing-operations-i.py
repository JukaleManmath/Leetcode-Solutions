class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0
        
        nums.sort()
        count = Counter(nums)
        minelem, maxelem = nums[0], nums[-1]
        ans = 0
        for i in range(minelem, maxelem + 1):
            l = bisect_left(nums, i - k)
            r = bisect_right(nums, i + k) - 1
            ans = max(ans , min(r - l + 1, numOperations + count[i]))
        return ans


       
        
