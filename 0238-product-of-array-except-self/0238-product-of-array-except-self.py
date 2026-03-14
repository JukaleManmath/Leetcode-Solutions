class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [0] * n
        s = [0] * n
        p[0] = 1
        s[n-1] = 1

        for i in range(1, n):
            p[i] = nums[i - 1] * p[i-1]
            s[n -1 -i] = nums[n - i] * s[n - i]
        res = [0] * n 
        for i in range(n):
            res[i] = p[i] * s[i]
        return res