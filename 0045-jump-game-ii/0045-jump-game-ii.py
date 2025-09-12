class Solution:
    def jump(self, nums: List[int]) -> int:
        # near = far = jump = 0
        # while far < len(nums) - 1:
        #     farthest = 0
        #     for i in range(near, far + 1):
        #         farthest = max(farthest, i + nums[i])
        #     near = far + 1
        #     far = farthest
        #     jump += 1
        # return jump
        n = len(nums)
        dp = [0] * n

        for i in range(n-1):
            near = i + 1
            far = i + nums[i]
            for j in range(near, far+1):
                if j < n and not dp[j]:
                    dp[j] = 1+ dp[i]
            if far == n- 1:
                break
        return dp[n-1]
