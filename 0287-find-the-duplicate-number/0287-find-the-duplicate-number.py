class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force
        nums.sort()
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                return nums[i]
        return -1

        # # map
        # map = {}
        # for i in nums:
        #     map[i] = 1 + map.get(i,0)
        #     if map.get(i,0) > 1:
        #         return i
        # return -1

        #set
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)
        # return -1