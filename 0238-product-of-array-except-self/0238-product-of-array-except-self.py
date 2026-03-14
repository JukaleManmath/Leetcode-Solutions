class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [1] * n
        s = [1] * n
        p[0] = nums[0]
        s[n-1] = nums[n-1]

        for i in range(1, n):
            p[i] = nums[i] * p[i-1]
            s[n -1 -i] = nums[n -1-i] * s[n - i]
        res = []
        for i in range(n):
            curr = 1
            if i > 0:
                curr = curr * p[i-1]
            if i < n-1:
                curr = curr * s[i + 1]
            res.append(curr)
        return res