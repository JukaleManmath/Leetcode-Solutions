class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #options - add or subtract
        dp = {}
        def dfs(i, res):
            if i >= len(nums) and res != target:
                return 0
            if i == len(nums) and res == target:
                return 1
            if (i,res) in dp:
                return dp[(i,res)]
            dp[(i,res)] =  dfs(i + 1 , res + nums[i]) + dfs(i+1, res - nums[i])
            return dp[(i,res)]

        return dfs(0, 0)
            