class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        arr = nums[1:]
        arr.sort()
        return nums[0] + arr[0] + arr[1]