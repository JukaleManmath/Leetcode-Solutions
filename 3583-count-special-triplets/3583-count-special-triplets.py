class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter(nums)
        track = defaultdict(int)
        res = 0
        mod = 10 ** 9 + 7

        for num in nums:
            first , last = 2 * num , 2 * num
            cnt[num] -= 1
            if track[first] > 0 and cnt[last] > 0:
                res = (res + (track[first] * cnt[last])) % mod
            track[num] += 1
            
        return res % mod