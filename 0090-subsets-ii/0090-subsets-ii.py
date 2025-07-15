class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i, curr):
            if i == len(nums):
                if curr not in res:
                    res.append(curr.copy())
                return
            
            dfs(i+1, curr)
            curr.append(nums[i])
            
            dfs(i+1, curr)
            curr.pop()
            
        dfs(0, subset)
        return res
