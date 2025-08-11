class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute force
        # res = float("-inf")
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(i,len(nums)):
        #         prod = prod * nums[j]
        #         res= max(res, prod)
        # return res
        
        #  prefix suffix 
        # res = float("-inf")
        # p = s = 0
        # n = len(nums)

        # for i in range(n):
        #     p = nums[i] * (p or 1)
        #     s = nums[n-1-i] * (s or 1)
        #     res = max(res, max(p,s))
        # return res
        
        # Kadane's algo for 1D dp problems
        res =nums[0]
        maxprod = minprod = 1
        n = len(nums)
        for i in range(n):
            x = nums[i]
            temp = x * maxprod
            maxprod = max(x, x * maxprod, x*minprod)
            minprod = min(x, temp, x*minprod)
            res = max(res, maxprod)
        return res