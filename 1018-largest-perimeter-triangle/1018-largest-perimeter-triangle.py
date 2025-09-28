class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        for i in range(n-1, 1, -1):
            l , r = i - 2 , i -1
            if nums[l] + nums[r] > nums[i]:
                return nums[l] + nums[r] + nums[i]
        return 0
