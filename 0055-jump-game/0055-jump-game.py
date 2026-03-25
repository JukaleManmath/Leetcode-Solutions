class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # target = n - 1
        # for i in range(n - 2, -1, -1):
        #     if i + nums[i] >= target:
        #         target = i
            
        # return target == 0

        canJump = 0
        for i in range(n- 1):
            if canJump < i:
                return False
            canJump = max(canJump ,i + nums[i])
        return canJump >= n - 1