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
        
        res = float("-inf")
        p = s = 0
        n = len(nums)

        for i in range(n):
            p = nums[i] * (p or 1)
            s = nums[n-1-i] * (s or 1)
            res = max(res, max(p,s))
        return res
 