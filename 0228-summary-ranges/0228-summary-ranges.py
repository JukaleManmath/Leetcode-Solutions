class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        l , r = 0 , 0
        res = []
        n = len(nums)
        while r < n -1:
            if nums[r] + 1 == nums[r + 1]:
                r = r + 1
            else:
                if r == l:
                    res.append(str(nums[l]))
                    l = r = r + 1
                else:
                    res.append(str(nums[l]) + "->"+str(nums[r]))
                    l = r + 1
                    r = r + 1
        if l == r:
            res.append(str(nums[r]))
        else:
            res.append(str(nums[l]) + "->"+str(nums[r]))
        return res  