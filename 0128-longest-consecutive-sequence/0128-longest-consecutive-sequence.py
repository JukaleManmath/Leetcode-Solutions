class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums= set(nums)
        max_length = 0
        for num in nums:
            if num -1 not in nums:
                count = 1
                while num+count in nums:
                    count += 1
                max_length = max(max_length, count)
        return max_length