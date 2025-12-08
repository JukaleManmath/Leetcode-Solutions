class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(idx, arr):
            if idx >= n:
                res.append(arr[:])
                return
            arr.append(nums[idx])
            backtrack(idx + 1, arr)
            arr.pop()
            backtrack(idx + 1, arr)
            
        backtrack(0, [])
        return res
