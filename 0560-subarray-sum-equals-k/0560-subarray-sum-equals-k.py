class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = 0
        mp = defaultdict(int)
        mp[0] = 1
        res = 0
        for i in range(n):
            p += nums[i]
            res += mp[p - k]
            mp[p] += 1
        return res