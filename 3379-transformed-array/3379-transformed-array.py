class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] == 0:
                res.append(nums[i])
            elif nums[i] > 0:
                idx = (i + nums[i]) % n
                res.append(nums[idx])
            elif nums[i] < 0:
                idx = (n + i + nums[i]) % n
                res.append(nums[idx])
        return res