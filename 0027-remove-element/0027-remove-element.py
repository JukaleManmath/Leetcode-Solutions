class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l , r = 0 , len(nums) -1
        while l < r:
            if nums[l] == val and nums[r] != val:
                nums[l] , nums[r] = nums[r] , nums[l]
                r -= 1
                l += 1
            elif nums[r] == val:
                r -= 1
            else:
                l += 1
        res , i = 0, 0
        while i < len(nums):
            if nums[i] == val:
                break
            i += 1
            res += 1
        return res
