class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        
        longest = 2
        l = -1
        for i in range(2 , len(nums)):
            if nums[i-2] + nums[i - 1] == nums[i]:
                if l == -1:
                    l = i - 2
                longest = max(longest , i - l + 1)
            else:
                l = -1
        return longest
