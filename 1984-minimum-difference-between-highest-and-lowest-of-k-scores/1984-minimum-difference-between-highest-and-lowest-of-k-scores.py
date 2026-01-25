class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mindiff = float("inf")
        for i in range(n- k + 1):
            mindiff = min(mindiff, nums[i + k -1] - nums[i])
        return mindiff
        