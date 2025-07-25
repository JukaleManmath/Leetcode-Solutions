class Solution:        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs_rec(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # exploring the choice
            subset.append(nums[i])
            dfs_rec(i + 1)

            #backtracking the choice
            subset.pop()
            dfs_rec(i + 1)
        
        dfs_rec(0)
        return res
