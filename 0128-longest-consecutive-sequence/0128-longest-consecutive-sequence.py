class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        res = 0
        for num in nums:
            if num -1 not in nums:
                cnt = 1
                while num + cnt in nums:
                    cnt += 1
                res = max(res, cnt)
        return res

            