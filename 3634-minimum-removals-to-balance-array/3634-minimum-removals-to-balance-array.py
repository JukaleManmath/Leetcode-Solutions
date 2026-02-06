class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = float("inf")
        l ,r = 0 , 0
        while r < n:
            if nums[r] <= k * nums[l]:
                r += 1
            elif nums[r] > k * nums[l]:
                curr = n - r +  l
                if curr < res:
                    res = curr
                l += 1
        res = min(res, n - r + l)
        return res if res != float("inf") else 0

        
