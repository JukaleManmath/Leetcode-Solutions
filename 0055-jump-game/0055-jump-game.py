class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canjump = 0
        n = len(nums)
        for i in range(n-1):
            if canjump == i and nums[i] == 0:
                return False
            canjump = max(canjump,i + nums[i])
        return canjump >= n -1