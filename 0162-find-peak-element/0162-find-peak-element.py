class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        # p = s = [True] * n

        # for i in range(1, n):
        #     if nums[i] < nums[i-1]:
        #         p[i] = False
            
        #     if nums[n-1-i] < nums[n-1-i+1]:
        #         s[n-1-i] = False
        
        # for i in range(n):
        #     if p[i] and s[i]:
        #         return i
        # return -1

        l , r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid - 1] < nums[mid]  and nums[mid + 1] < nums[mid]:
                return mid
            elif nums[mid + 1] < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l
        
        