class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []
        def backtrack(idx):
            if idx >= n:
                if subset not in res:
                    res.append(subset[:])
                return
            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()
            backtrack(idx + 1)
            
        backtrack(0)
        return res
