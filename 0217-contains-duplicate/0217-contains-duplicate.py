class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))

        # new_Set = set()

        # for num in nums:
        #     if num in new_Set:
        #         return True
        #     new_Set.add(num)
        # return False