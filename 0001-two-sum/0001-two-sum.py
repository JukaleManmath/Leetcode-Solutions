class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            tar = target - nums[i]
            if nums[i] in mp:
                return [mp[nums[i]], i]
            mp[tar] = i
        