class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        i , j = 0, 0
        while i < n:
            if nums[i] not in s:
                nums[j] = nums[i]
                s.add(nums[i])
                j += 1
            i += 1
        return j

        