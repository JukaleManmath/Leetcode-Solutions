class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []
        nums.sort()

        def backtrack(i):
            if i >= n:
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            while i+ 1 < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
            
        backtrack(0)
        return res
