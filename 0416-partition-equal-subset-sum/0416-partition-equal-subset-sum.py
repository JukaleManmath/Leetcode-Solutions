class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        s = 0
        for num in nums:
            s += num
        if s % 2 != 0:
            return False
        target = s // 2

        t = [[False] * (target + 1) for i in range(len(nums)+1)]
        for i in range(len(nums) + 1):
            for j in range(target + 1):
                if j == 0:
                    t[i][j] = True

        
        for i in range(1, len(nums)+1):
            for j in range(1, target + 1):
                if nums[i-1] <= j:
                    t[i][j] = t[i-1][j- nums[i-1]] or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        
        return t[len(nums)][target]