class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # n = len(nums)

        # res = nums[0]

        # for i in range(n):
        #     curr = nums[i]
        #     idx = (i + 1) % n
        #     while idx != i:
        #         curr = max(curr + nums[idx], nums[idx])
        #         res = max(res, curr)
        #         idx = (idx +1) % n
        # return res

        total , currmax, maxsum,  currmin, minsum = nums[0] , nums[0], nums[0], nums[0], nums[0]

        for i in nums[1:]:
            currmax = max(currmax + i , i)
            currmin = min( currmin + i, i)
            maxsum = max(maxsum, currmax)
            minsum  = min(minsum, currmin)
            total += i
        return max(total - minsum, maxsum) if maxsum > 0 else maxsum
