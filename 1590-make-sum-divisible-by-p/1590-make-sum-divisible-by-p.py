class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)

        remain = total % p

        if remain == 0:
            return 0
        
        res = len(nums)
        cur_sum = 0
        mp = {0:-1}
        for i , n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            prefix = (cur_sum - remain + p) % p
            if prefix in mp:
                length = i - mp[prefix]
                res = min(res, length)
            mp[cur_sum] = i


        return -1 if res == len(nums) else res
